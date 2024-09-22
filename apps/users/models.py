from apps.users.managers import CustomUserManager
from apps.common.models import  BaseModel

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, BaseModel):
    first_name = None
    last_name = None
    email = None
    created_at = None
    updated_at = None

    full_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to='user_profile/', blank=True, null=True)
    coins = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name", "phone_number"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.full_name
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        super().save(force_insert, force_update, using, update_fields)
        if self.is_deleted:
            self.phone_number = f'{self.phone_number}-deleted-{self.id}'
            self.save()


class Address(BaseModel):
    name = models.CharField(max_length=40)
    entrance = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    home_number = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.user:
            return '-'.join([self.name, self.user.full_name])
        return '-'.join([self.name, "Unidentified"])

