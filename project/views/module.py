from project.serializers import ProjectModuleSerializer, ProjectModuleListSerializer
from project.models import ProjectModule
from rest_framework import viewsets
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupObjectPermissionSerializer


class ProjectModuleViewSet(viewsets.ModelViewSet):
    queryset = ProjectModule.objects.all()
    serializer_class = ProjectModuleSerializer


class ProjectModuleListSet(viewsets.ModelViewSet):
    queryset = ProjectModule.objects.all()
    serializer_class = ProjectModuleListSerializer
    filterset_fields = ('project',)


# ProjectModule Perm
class ProjectModulePermViewSet(viewsets.ModelViewSet):
    queryset = ProjectModule.objects.all()
    serializer_class = ProjectModuleListSerializer

    def list(self, request, *args, **kwargs):
        content_type = request.GET.get('content_type')
        group = request.GET.get('group')
        name = request.GET.get('name')
        queryset = ProjectModule.objects.filter(project__name__icontains=name)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h['project']['name'] + ':  ' + h.pop('name')
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
