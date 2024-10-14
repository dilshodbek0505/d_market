from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from apps.shop.models import ProductRating, Card

User = get_user_model()


@receiver(post_save, sender=ProductRating)
def add_rating(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        all_ratings = product.product.rating + instance.rating
        all_ratings_count = ProductRating.objects.select_related('product', 'user').filter(product__product=product.product).count()
        product.product.rating = all_ratings / all_ratings_count
        product.product.save()


@receiver(post_save, sender=User)
def add_card_to_user(sender, instance, created, **kwargs):
    if created:
        card = Card.objects.create(user=instance)
        
        


