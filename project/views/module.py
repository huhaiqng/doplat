from rest_framework import viewsets
from rest_framework.response import Response
from project.models import ProjectModule
from guardian.models import GroupObjectPermission
from project.serializers import ProjectModuleSerializer, ProjectModuleListSerializer
from authperm.serializers import GroupObjectPermissionSerializer


class ProjectModuleViewSet(viewsets.ModelViewSet):
    queryset = ProjectModule.objects.all()
    serializer_class = ProjectModuleSerializer
    filterset_fields = ('project',)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return ProjectModuleListSerializer
        return ProjectModuleSerializer

    def list(self, request, *args, **kwargs):
        with_perms = request.query_params.get('with_perms', 'false')
        content_type = request.query_params.get('content_type')
        group = request.query_params.get('group')
        name = request.query_params.get('name', '')
        queryset = ProjectModule.objects.filter(project__name__icontains=name)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # 设置对象权限需要对象权限
            if with_perms == 'true':
                for h in serializer.data:
                    perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                    h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                    h['perms'] = perms.values_list('permission', flat=True)
                    h['name'] = h['project']['name'] + ':  ' + h.pop('name')
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # 设置对象权限需要对象权限
        if with_perms == 'true':
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h['project']['name'] + ':  ' + h.pop('name')
        return Response(serializer.data)
