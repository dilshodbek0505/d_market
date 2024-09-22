from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from apps.users.api_endpoints.Address.serializers import AddressSerializer
from apps.users.models import Address


class AddressCreateApiView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class AddressRUDApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = 'pk'


class AddressListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressSerializer
    queryset = Address.objects.all()



__all__=[
    'AddressCreateApiView',
    'AddressRUDApiView',
    'AddressListApiView',
]