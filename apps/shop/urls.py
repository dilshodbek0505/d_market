from django.urls import path

from apps.shop.api_endpoints import *
from apps.shop.api_endpoints.Product.views import AddRatingApiView

app_name = "shop"

urlpatterns = [
    path('category/list/', CategoryListApi.as_view(), name='category-list'),

    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('product/rating/', AddRatingApiView.as_view(), name='product-rating'),
    
    path('order-item/add/', AddProductToOrderApi.as_view(), name='order-item-add'),
    path('order-item/update/<uuid:pk>/', UpdateOrderItemApi.as_view(), name='order-item-update'),

    path('order/list/', UserOrderListApi.as_view(), name='user-order-list'),
    path('order/add/', NewOrderApi.as_view(), name='new-order'),
    
    path('card-item/add/', CreateCardItemApi.as_view(), name='card-item-add'),
    path('card-item/update/<uuid:pk>/', UpdateCardItemApi.as_view(), name='card-item-update')
]
