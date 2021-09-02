from rest_framework import viewsets
from django.contrib.auth.models import Group
from authperm.serializers import GroupSerializer, GetGroupSerializer, GroupNameSerializer, \
    GroupObjectPermissionSerializer
from guardian.models import GroupObjectPermission
from rest_framework.permissions import IsAdminUser


# 增删改组
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupNameViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupNameSerializer
    pagination_class = None


# 查询组
class GetGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GetGroupSerializer


# 组对象权限
class GroupObjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = GroupObjectPermission.objects.all()
    serializer_class = GroupObjectPermissionSerializer
    permission_classes = [IsAdminUser]
