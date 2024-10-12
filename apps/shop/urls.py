from django.urls import path

from apps.shop.api_endpoints import *
from apps.shop.api_endpoints.Product.views import AddRatingApiView

app_name = "shop"

urlpatterns = [
    path('category/list/', CategoryListApi.as_view(), name='category-list'),

    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('product/rating/', AddRatingApiView.as_view(), name='product-rating'),

    path('user-order/list/', UserOrderListApi.as_view(), name='user-order-list'),
]