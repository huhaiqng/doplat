from rest_framework import viewsets
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from project.models import Host
from project.serializers import HostSerializer, GetHostSerializer, HostSimpleSerializer
from project.filters import HostFilter
from authperm.serializers import GroupObjectPermissionSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    filterset_class = HostFilter

    def get_serializer_class(self):
        if self.request.query_params.get('simple', False) == 'true':
            return HostSimpleSerializer
        if self.request.query_params.get('with_perms', False) == 'true':
            return HostSimpleSerializer
        if self.request.method.lower() == 'get':
            return GetHostSerializer
        return HostSerializer

    def list(self, request, *args, **kwargs):
        with_perms = request.query_params.get('with_perms', 'false')
        content_type = request.GET.get('content_type')
        group = request.GET.get('group')
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # 设置对象权限需要对象权限
            if with_perms == 'true':
                for h in serializer.data:
                    perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                    h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                    h['perms'] = perms.values_list('permission', flat=True)
                    h['name'] = h.pop('inside_ip')
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        if with_perms == 'true':
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h.pop('inside_ip')
        return Response(serializer.data)
