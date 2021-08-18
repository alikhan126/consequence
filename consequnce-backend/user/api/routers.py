from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from user.api.viewsets import (
    AuthUserRegistrationView,
    AuthUserLoginView,
    UserListView,
    WelcomeView,
    ForgotPasswordView,
    ForgotPasswordConfirmView,
    VerifyOTPView,
    ChangePasswordView,
    ProfileView,
)

router = routers.SimpleRouter()

urlpatterns = [
    url(r'auth/', include(router.urls)),
    path('auth/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('auth/register/', AuthUserRegistrationView.as_view(), name='register'),
    path('auth/login/', AuthUserLoginView.as_view(), name='login'),
    path('auth/users/', UserListView.as_view(), name='users'),
    path('auth/profile/', ProfileView.as_view(), name='profile-detail'),
    path('auth/welcome/', WelcomeView.as_view(), name='welcome'),
    path('auth/verify/otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('auth/forgot/password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('auth/forgot/password/confirm/', ForgotPasswordConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('auth/change/password/', ChangePasswordView.as_view(), name='change_password'),
    path('auth/password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
