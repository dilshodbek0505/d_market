from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.shop.api_endpoints.Order.serializers import OrderSerializer, OrderItemsSerializer, \
    CreateOrderItemsSerializer, CreateOrderSerializer
from apps.shop.models import Order, OrderItem


class UserOrderListApi(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class AddProductToOrderApi(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = OrderItem.objects.all()
    serializer_class = CreateOrderItemsSerializer

class UpdateOrderItemApi(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = OrderItem.objects.all()
    serializer_class = CreateOrderItemsSerializer
    
     
class NewOrderApi(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    
__all__ = [
    'UserOrderListApi',
    'AddProductToOrderApi',
    'NewOrderApi',
    'UpdateOrderItemApi'
]