from django.urls import path

from apps.user.api_endpoints import *

app_name = 'user'

urlpatterns = [
    path('login/', UserLoginApi.as_view(), name='login'),
    path('token/refresh/', RefreshTokenApi.as_view(), name='token_refresh'),
    path('register/', RegisterApi.as_view(), name='register'),
    path('login-confirm/', UserLoginConfirmApi.as_view(), name='login_confirm'),
    path('register-confirm/', RegisterConfirmApi.as_view(), name='register_confirm'),
    path('details/<uuid:pk>/', UserDetailsApi.as_view(), name='details'),
]