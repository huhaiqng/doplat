from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import Group
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupSerializer, GetGroupSerializer, GroupNameSerializer, \
     GroupObjectPermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.request.query_params.get('name', False) == 'true':
            return GroupNameSerializer
        if self.request.method.lower() == 'get':
            return GetGroupSerializer
        return GroupSerializer

    def list(self, request, *args, **kwargs):
        if self.request.query_params.get('name', False) == 'true':
            self.pagination_class = None

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 组对象权限
class GroupObjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = GroupObjectPermission.objects.all()
    serializer_class = GroupObjectPermissionSerializer
    permission_classes = [IsAdminUser]
