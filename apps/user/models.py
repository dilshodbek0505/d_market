from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.tokens import RefreshToken

from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel



class User(BaseModel, AbstractUser):
    email = models.EmailField(_('email address'), unique=True, blank=True, null=True)
    phone_number = PhoneNumberField(_('phone number'), region="UZ", unique=True)
    coins = models.PositiveIntegerField(default=0, help_text=_('User coins'))
    telegram_id = models.PositiveIntegerField(default=0, help_text=_('Telegram id'))
    
    def __str__(self):
        return self.username

    @property
    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
