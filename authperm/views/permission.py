from rest_framework import viewsets
from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAdminUser
from authperm.serializers import PermissionSerializer


# 组对象权限
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filterset_fields = ('content_type',)
    permission_classes = [IsAdminUser]
