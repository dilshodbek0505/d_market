from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.shop.api_endpoints.Order.serializers import UserOrderSerializer
from apps.shop.models import Order


class UserOrderListApi(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = UserOrderSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

__all__ = [
    'UserOrderListApi',
]