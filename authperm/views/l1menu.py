from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from authperm.models import L1Menu
from authperm.serializers import L1MenuSerializer, L1MenuListSerializer
from authperm.filters import L1MenuFilter
from django_filters.rest_framework import DjangoFilterBackend


# 增删改
class L1MenuViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuSerializer


# List
class L1MenuListViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuListSerializer
    filterset_class = L1MenuFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
