from django.contrib import admin

from apps.shop.models import Category, Product, ProductImage, Order, OrderItem, ProductSize, ProductRating, \
    Card, CardItem


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ProductSize)
admin.site.register(ProductRating)
admin.site.register(Card)
admin.site.register(CardItem)
