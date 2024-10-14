from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.user.api_endpoints.UserDetails.serializsers import UserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetailsApi(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user


__all__ = [
    'UserDetailsApi',
]
