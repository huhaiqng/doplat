from rest_framework import viewsets
from project.models import Env
from project.serializers import EnvSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# 环境
class EnvViewSet(viewsets.ModelViewSet):
    queryset = Env.objects.all().order_by('name')
    serializer_class = EnvSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
