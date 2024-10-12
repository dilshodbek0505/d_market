from rest_framework import serializers

from apps.shop.models import Product, ProductSize, ProductImage, ProductRating
from apps.shop.api_endpoints.Category.serializers import CategorySerializer


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ('id', 'size', 'price')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ('user', 'product', 'rating')
        extra_kwargs = {'user': {'required': False}}


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    sizes = ProductSizeSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'rating', 'sizes', 'images')
