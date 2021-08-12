from project.serializers import ConfigSerializer, GetConfigSerializer
from project.models import Config
from rest_framework import viewsets


class GetConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = GetConfigSerializer
    filterset_fields = ('project',)


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
