from rest_framework import viewsets
from authperm.models import L2Menu
from authperm.serializers import L2MenuSerializer, L2MenuContentTypeSerializer, L2MenuListSerializer
from authperm.filters import L2MenuFilter


# 增删改
class L2MenuViewSet(viewsets.ModelViewSet):
    queryset = L2Menu.objects.all()
    serializer_class = L2MenuSerializer


# List
class L2MenuListViewSet(viewsets.ModelViewSet):
    queryset = L2Menu.objects.all()
    serializer_class = L2MenuListSerializer
    filterset_class = L2MenuFilter


class L2MenuContentTypeViewSet(viewsets.ModelViewSet):
    queryset = L2Menu.objects.filter(content_type__isnull=False)
    serializer_class = L2MenuContentTypeSerializer
