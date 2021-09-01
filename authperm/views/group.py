from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from guardian.models import GroupObjectPermission
from django.contrib.auth.models import Group, ContentType
from authperm.serializers import GroupSerializer, GetGroupSerializer, GroupObjectPermissionSerializer, \
    GroupNameSerializer
from django.contrib.auth.models import Permission
from authperm.filters import GroupObjectPermissionFilter


# 增删改组
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupNameViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupNameSerializer


# 查询组
class GetGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GetGroupSerializer


# 获取组拥有权限的二级菜单
class GetGroupL2menuView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        groupname = request.GET.get('groupname')
        group = Group.objects.get(name=groupname)
        # 查询组的模型 l2menu 查看权限所有记录
        permission_pk = Permission.objects.get(codename='view_l2menu').id
        queryset = GroupObjectPermission.objects.filter(group=group, permission=permission_pk).values('object_pk')
        results = []
        for obj in queryset:
            results.append(int(obj['object_pk']))
        return Response(results)


# 组对象权限
class GroupObjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = GroupObjectPermission.objects.all()
    serializer_class = GroupObjectPermissionSerializer
    filterset_class = GroupObjectPermissionFilter
    permission_classes = [IsAdminUser]
