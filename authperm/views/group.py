from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from guardian.models import GroupObjectPermission
from django.contrib.auth.models import Group, ContentType
from authperm.serializers import GroupSerializer, GetGroupSerializer, GroupObjectPermissionSerializer, \
    GroupNameSerializer
from django_filters.rest_framework import DjangoFilterBackend


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


# 设置组的权限
class SetGroupObjectPermsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, format=None):
        model = request.data['model']
        content_type = ContentType.objects.get(model=model)
        objects = request.data['objects']
        groupname = request.data['groupname']
        group = Group.objects.get(name=groupname)
        content_type_id = content_type.id
        group_id = group.id
        for i, object in enumerate(objects):
            object_pk = int(object['id'])
            # 已存在的权限
            e_perms = GroupObjectPermission.objects.filter(content_type_id=content_type_id,
                                                           object_pk=object_pk,
                                                           group_id=group_id)
            # 删除已存在的权限
            e_perms.delete()
            perms = object['perms']
            for permission_id in perms:
                gop = GroupObjectPermission(content_type_id=content_type_id,
                                            object_pk=object_pk,
                                            group_id=group_id,
                                            permission_id=permission_id)
                gop.save()
        return Response(status=status.HTTP_201_CREATED)


# 获取组拥有权限的二级菜单
class GetGroupL2menuView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        groupname = request.GET.get('groupname')
        group = Group.objects.get(name=groupname)
        # 查询组的模型 l2menu 查看权限所有记录
        queryset = GroupObjectPermission.objects.filter(group=group, permission=104).values('object_pk')
        results = []
        for obj in queryset:
            results.append(int(obj['object_pk']))
        return Response(results)


# 组对象权限
class GroupObjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = GroupObjectPermission.objects.all()
    serializer_class = GroupObjectPermissionSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
