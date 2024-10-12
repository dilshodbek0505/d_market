from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from apps.shop.api_endpoints.Category.serializers import CategorySerializer
from apps.shop.models import Category


class CategoryListApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = None


__all__ = ['CategoryListApi']
