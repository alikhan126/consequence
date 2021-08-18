from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from allauth.account.views import sensitive_post_parameters_m, ConfirmEmailView
from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.api.serializers import (
    UserLoginSerializer,
    UserListSerializer,
    RegisterSerializer,
    ForgotPasswordSerializer,
    ForgotPasswordConfirmSerializer,
    VerifyOTPSerializer,
    ChangePasswordSerializer,
    ProfileDetailSerializer,
    VerifyEmailSerializer,
)
from user.models import User


class AuthUserRegistrationView(APIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        status_code = status.HTTP_200_OK

        response = {
            'success': True,
            'statusCode': status_code,
            'message': 'User successfully registered!',
            'user': serializer.data
        }

        return Response(response, status=status_code)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        complete_signup(
            self.request._request, user,
            allauth_settings.EMAIL_VERIFICATION,
            None)


class AuthUserLoginView(APIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserListView(APIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        if user and user.role != 1:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            users = User.objects.all()
            serializer = self.serializer_class(users, many=True)
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Successfully fetched users',
                'users': serializer.data

            }
            return Response(response, status=status.HTTP_200_OK)


class WelcomeView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Welcome to the PMS',
            'data': "Email Verified Successfully"
        }
        return Response(response, status=status.HTTP_200_OK)


class ForgotPasswordView(GenericAPIView):
    """
    Calls Django Auth PasswordResetForm save method.
    Accepts the following POST parameters: email
    Returns the success/fail message.
    """

    serializer_class = ForgotPasswordSerializer
    permission_classes = (AllowAny,)

    def post(
            self,
            request,
            *args,
            **kwargs
    ):
        # Create a serializer with request.data

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({'detail': 'Password reset e-mail has been sent.'
                         }, status=status.HTTP_200_OK)


class ForgotPasswordConfirmView(GenericAPIView):
    """
    Password reset e-mail link is confirmed, therefore
    this resets the user's password.
    Accepts the following POST parameters: token, uid,
        new_password1, new_password2
    Returns the success/fail message.
    """

    serializer_class = ForgotPasswordConfirmSerializer
    permission_classes = (AllowAny,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(ForgotPasswordConfirmView, self).dispatch(*args, **kwargs)

    def post(
            self,
            request,
            *args,
            **kwargs
    ):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'detail': 'Password has been reset with the new password.'
                         })


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = VerifyOTPSerializer

    def post(
            self,
            request,
            *args,
            **kwargs
    ):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'detail': 'OTP Verified.'}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    """
    API View to get User Profile Detail by sending the unique id of the user.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileDetailSerializer

    def get(self, request):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return Response(data={"error": "You don't have the permission to access."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(
            self,
            request,
            *args,
            **kwargs
    ):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.kwargs['key'] = serializer.validated_data['key']
            confirmation = self.get_object()
            confirmation.confirm(self.request)
            return Response({'detail': 'Email Verification Successful'
                             }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    'detail': 'This e-mail confirmation link expired or is invalid.'
                }, status=status.HTTP_400_BAD_REQUEST)
