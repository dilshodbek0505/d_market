from django.contrib import admin

from apps.shop.models import Category, Product, ProductImage, Order, OrderItem, ProductSize, ProductRating


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ProductSize)
admin.site.register(ProductRating)