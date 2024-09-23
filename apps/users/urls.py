from django.urls import path
from apps.users.api_endpoints.UserAuth.views import (
    LoginOtp,
    RegisterOtp,
    ConfirmOtp,
    Register,
    UserDetail,
)
from apps.users.api_endpoints.Address.views import (
    AddressListApiView,
    AddressCreateApiView,
    AddressRUDApiView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # user url endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', Register.as_view()),
    path('register-otp/', RegisterOtp.as_view()),
    path('login-otp/', LoginOtp.as_view()),
    path('confirm-otp/', ConfirmOtp.as_view()),
    path('details/<uuid:pk>/', UserDetail.as_view()),

    # address url endpoints
    path('address-create/', AddressCreateApiView.as_view()),
    path('address-list/', AddressListApiView.as_view()),
    path('address-details/<uuid:pk>/', AddressRUDApiView.as_view()),
]

