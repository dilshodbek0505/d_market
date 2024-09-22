from rest_framework import serializers

from apps.users.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("id", "name", "entrance", "floor", "home_number", "comment", "user")
