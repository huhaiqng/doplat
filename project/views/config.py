from project.serializers import ConfigSerializer, GetConfigSerializer
from project.models import Config
from rest_framework import viewsets
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupObjectPermissionSerializer


class GetConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = GetConfigSerializer
    filterset_fields = ('project',)


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


# Config Perm
class ConfigPermViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = GetConfigSerializer

    def list(self, request, *args, **kwargs):
        content_type = request.GET.get('content_type')
        group = request.GET.get('group')
        name = request.GET.get('name')
        queryset = Config.objects.filter(project__name__icontains=name)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h['env']['name'] + ': ' + h['project']['name']
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
