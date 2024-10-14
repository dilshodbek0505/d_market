from rest_framework import serializers

from apps.shop.api_endpoints.Card.serializers import CardSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    card = CardSerializer(required = False)
    class Meta:
        model = User
        fields = ('id', 'username', 'phone_number', 'first_name', 'last_name', 'coins', 'card')
        read_only_fields = ['card', 'coins']

    
