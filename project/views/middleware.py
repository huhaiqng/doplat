from rest_framework import viewsets
from project.serializers import MiddlewareSerializer, MiddlewareListSerializer
from project.models import Middleware
from project.filters import MiddlewareFilter


# 增删改
class MiddlewareViewSet(viewsets.ModelViewSet):
    queryset = Middleware.objects.all()
    serializer_class = MiddlewareSerializer


# 列表
class MiddlewareListViewSet(viewsets.ModelViewSet):
    queryset = Middleware.objects.all()
    serializer_class = MiddlewareListSerializer
    filterset_class = MiddlewareFilter
