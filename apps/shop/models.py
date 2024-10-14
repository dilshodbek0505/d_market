from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum, F
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


User = get_user_model()

TYPE = (
    ('fast-food', 'fast-food'),
    ('food', 'food')
)


class Category(BaseModel):
    name = models.CharField(max_length=128, unique=True, help_text=_('Category name'))
    category_type = models.CharField(max_length=128, choices=TYPE,help_text=_('Category type'))
    icon = models.ImageField(upload_to='categories', help_text=_('Category icon'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(BaseModel):
    name = models.CharField(max_length=128, help_text=_('Product name'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text=_('Category name'), related_name='products')
    about = models.TextField(help_text=_('Product description'), blank=True)
    rating = models.FloatField(default=0, help_text=_('Product rating'))

    def __str__(self):
        return self.name


class ProductSize(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text=_('Product name'), related_name='sizes')
    size = models.CharField(max_length=128, help_text=_('Product size'))
    price = models.DecimalField(max_digits=40, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0, help_text=_('Product stock'))


    def __str__(self, *args, **kwargs):
        return self.product.name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text=_('Product name'), related_name='images')
    image = models.ImageField(upload_to='products', help_text=_('Product image'))

    def __str__(self):
        return self.product.name


class ProductRating(BaseModel):
    product = models.ForeignKey(ProductSize, on_delete=models.CASCADE, help_text=_('Product name'), related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_('User'), related_name='ratings')
    rating = models.FloatField(default=0, help_text=_('Rating'))

    def __str__(self):
        return f"{self.product.product.name} | {self.rating}"

STATUS = (
    ('padding', 'padding' ),
    ('shipping', 'shipping' ),
    ('delivered', 'delivered' ),
    ('canceled', 'canceled')
)

ORDER = (
    ('cash', 'cash'),
    ('card', 'card')
)

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_('User'), related_name='orders')
    status = models.CharField(max_length=128, choices=STATUS, help_text=_('Order status'))
    order_type = models.CharField(max_length=128, choices=ORDER, help_text=_('Order type'))

    def __str__(self):
        return self.user.username


class OrderItem(BaseModel):
    product = models.ForeignKey(ProductSize, on_delete=models.CASCADE, help_text=_('Product name'), related_name='items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text=_('Order'), related_name='items')
    quantity = models.PositiveIntegerField(help_text=_('Quantity'), default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.product.name


class Card(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text=_('User card'), related_name='card')
    
    def __str__(self) -> str:
        return self.user.username


class CardItem(BaseModel):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, help_text=_('Card items'), related_name='card_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text=_('Card product'), related_name='card_items')
    
    def __str__(self) -> str:
        return f'{self.card.user.username} | {self.product.name}'

    
