from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from app.serializers import AddressSerializer
from app.models import Address
from django_filters.rest_framework import DjangoFilterBackend


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
    pagination_class = None
