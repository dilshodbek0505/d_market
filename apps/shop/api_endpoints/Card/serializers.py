from rest_framework import serializers

from apps.shop.models import Card, CardItem
from apps.shop.api_endpoints.Product.serializers import ProductSerializer


class CardItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CardItem
        fields = ('id', 'product')
        
        
class CardSerializer(serializers.ModelSerializer):
    card_items = CardItemSerializer(many=True)
    class Meta:
        model = Card
        fields = ('id', 'card_items')
    
    
class CreateCardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = ('id', 'product', 'card')
        