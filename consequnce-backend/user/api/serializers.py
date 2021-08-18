from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.forms import SetPasswordForm
from allauth.account.models import EmailAddress
from allauth.account.utils import (
    setup_user_email, send_email_confirmation
)
from allauth.utils import email_address_exists
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import update_last_login
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode as uid_decoder
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import PasswordField
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from user.models import User

UserModel: object = get_user_model()


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    phone_number = serializers.CharField(required=False)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    "A user is already registered with this e-mail address."
                )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'username': self.validated_data.get('username', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        user.set_password(request.data['password1'])
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = PasswordField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    full_name = serializers.CharField(max_length=255, read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        email_address = EmailAddress.objects.filter(
            user=user, verified=True).exists()
        if not email_address:
            request = self.context['request']
            send_email_confirmation(request, user)
            msg = "Please verify your email to login"
            raise serializers.ValidationError({"message": msg})

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'id': user.id,
                'role': user.role,
                'full_name': user.full_name,
                'username': user.username
            }
            login(self.context['request'], user, backend='django.contrib.auth.backends.ModelBackend')

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'role'
        )


class ForgotPasswordSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    email = serializers.EmailField()

    password_reset_form_class = PasswordResetForm

    def get_email_options(self):
        """Override this method to change default e-mail options"""
        return {}

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        user = User.objects.filter(email=value)
        if user:
            self.reset_form = self.password_reset_form_class(data=self.initial_data)
            if not self.reset_form.is_valid():
                raise serializers.ValidationError(self.reset_form.errors)
        else:
            raise serializers.ValidationError("No User associated with this email.")
        return value

    def save(self):
        request = self.context.get('request')

        # Set some values to trigger the send_email method.
        domain = f'{settings.FRONT_URL}/reset-password'
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
            'domain_override': domain,
            'subject_template_name': 'account/email/password_reset_key_subject.txt',
            'email_template_name': 'account/email/password_reset_key_message.txt',
            'html_email_template_name': 'account/email/password_reset_key_message.txt'
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)


class ForgotPasswordConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    password1 = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()

    set_password_form_class = SetPasswordForm

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        self._errors = {}

        # Decode the uidb64 to uid to get User object
        try:
            uid = force_text(uid_decoder(attrs['uid']))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid value']})
        user = self.user
        user.is_active = True
        user.set_password(attrs['password1'])
        user.save()
        return attrs

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)


class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=50)
    otp = serializers.CharField(required=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        code = attrs.get('otp', '')
        phone_number = attrs.get('phone_number', '')

        user = User.objects.filter(phone_number=phone_number).first()
        if user:
            user.phone_number_verified = True
            user.save()

        return attrs


class ProfileDetailSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
            "date_joined",
            "is_active",
            "phone_number",
            "phone_number_verified"
        )

        extra_kwargs = {
            "id": {"read_only": True},
            "role": {"read_only": True},
            "is_active": {"read_only": True},
            "phone_number_verified": {"read_only": True},
            "date_joined": {"read_only": True},
        }


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()
