from rest_framework import viewsets
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from project.models import Config
from project.serializers import ConfigSerializer, GetConfigSerializer
from authperm.serializers import GroupObjectPermissionSerializer


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    filterset_fields = ('project',)

    def get_queryset(self):
        with_perms = self.request.query_params.get('with_perms', 'false')
        name = self.request.query_params.get('name', '')
        if with_perms == 'true':
            queryset = Config.objects.filter(project__name__icontains=name)
        else:
            queryset = Config.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return GetConfigSerializer
        return ConfigSerializer

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
                    h['name'] = h['env']['name'] + ': ' + h['project']['name']
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        if with_perms == 'true':
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h['env']['name'] + ': ' + h['project']['name']
        return Response(serializer.data)
