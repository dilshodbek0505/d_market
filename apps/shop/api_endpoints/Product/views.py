from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.shop.models import Product, ProductRating
from apps.shop.api_endpoints.Product.serializers import ProductSerializer, ProductRatingSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class AddRatingApiView(CreateAPIView):
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

__all__ = [
    'ProductListAPIView',
]