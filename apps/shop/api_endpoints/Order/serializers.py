from rest_framework import serializers

from django.db.models import Sum

from apps.shop.models import Order, OrderItem, Product
from apps.shop.api_endpoints.Product.serializers import ProductSerializer, ProductSizeSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    product = ProductSizeSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'total_price')


    def get_total_price(self, obj):
        return obj.total_price


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True, required=False)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ('id', 'status', 'order_type', 'items', 'total_price')


    def get_total_price(self, obj):
        return sum([item.total_price for item in obj.items.all()])
        
        
class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status', 'order_type')
        
        
class CreateOrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'order', 'quantity')