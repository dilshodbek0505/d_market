from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.shop.models import ProductRating

@receiver(post_save, sender=ProductRating)
def add_rating(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        all_ratings = product.product.rating + instance.rating
        all_ratings_count = ProductRating.objects.select_related('product', 'user').filter(product__product=product.product).count()
        product.product.rating = all_ratings / all_ratings_count
        product.product.save()

