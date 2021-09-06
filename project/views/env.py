from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from project.models import Env
from project.serializers import EnvSerializer


# 环境
class EnvViewSet(generics.ListAPIView):
    queryset = Env.objects.all().order_by('name')
    serializer_class = EnvSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    pagination_class = None
