from rest_framework import viewsets
from authperm.models import L2Menu
from authperm.serializers import L2MenuSerializer, L2MenuContentTypeSerializer


# 二级模型菜单
class L2MenuViewSet(viewsets.ModelViewSet):
    queryset = L2Menu.objects.all()
    serializer_class = L2MenuSerializer


class L2MenuContentTypeViewSet(viewsets.ModelViewSet):
    queryset = L2Menu.objects.filter(content_type__isnull=False)
    serializer_class = L2MenuContentTypeSerializer
