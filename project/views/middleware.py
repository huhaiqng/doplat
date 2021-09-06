from rest_framework import viewsets
from project.serializers import MiddlewareSerializer, MiddlewareListSerializer
from project.models import Middleware
from project.filters import MiddlewareFilter
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupObjectPermissionSerializer


class MiddlewareViewSet(viewsets.ModelViewSet):
    queryset = Middleware.objects.all()
    serializer_class = MiddlewareSerializer
    filterset_class = MiddlewareFilter

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return MiddlewareListSerializer
        return MiddlewareSerializer

    def list(self, request, *args, **kwargs):
        with_perms = request.query_params.get('with_perms', 'false')
        content_type = request.query_params.get('content_type')
        group = request.query_params.get('group')
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
                    h['name'] = h.pop('conn_addr')
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # 设置对象权限需要对象权限
        if with_perms == 'true':
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h.pop('conn_addr')
        return Response(serializer.data)
