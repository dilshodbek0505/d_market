from rest_framework import serializers

from apps.shop.models import Order, OrderItem, Product
from apps.shop.api_endpoints.Product.serializers import ProductSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'total_price')

    @staticmethod
    def get_total_price(obj):
        return obj.total_price

class UserOrderSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True)
    class Meta:
        model = Order
        fields = ('id', 'status', 'order_type', 'items')
