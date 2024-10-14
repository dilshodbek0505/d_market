from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.shop.api_endpoints.Card.serializers import CardSerializer, CreateCardItemSerializer
from apps.shop.models import Card, CardItem


class CreateCardItemApi(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = CardItem.objects.all()
    serializer_class = CreateCardItemSerializer

class UpdateCardItemApi(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = CardItem.objects.all()
    serializer_class = CreateCardItemSerializer
    
    
__all__ = [
    'CreateCardItemApi',
    'UpdateCardItemApi'
    
]