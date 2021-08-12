from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from authperm.models import L1Menu
from authperm.serializers import L1MenuSerializer
from django_filters.rest_framework import DjangoFilterBackend


# 一级菜单
class L1MenuViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
