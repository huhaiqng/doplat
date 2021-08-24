from rest_framework import viewsets
from project.serializers import HostSerializer, GetHostSerializer, HostSimpleSerializer
from project.models import Host
from project.filters import HostFilter


# 增删改
class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


# List
class GetHostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = GetHostSerializer
    filterset_class = HostFilter


# Host Simple
class HostSimpleViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSimpleSerializer
