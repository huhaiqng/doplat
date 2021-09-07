from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import Permission
from authperm.serializers import PermissionSerializer


# 组对象权限
class PermissionViewSet(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filterset_fields = ('content_type',)
    permission_classes = [IsAdminUser]
    pagination_class = None
