from rest_framework import viewsets
from project.serializers import HostSerializer, GetHostSerializer, HostSimpleSerializer
from project.models import Host
from project.filters import HostFilter
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupObjectPermissionSerializer


# 增删改
class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


# List
class GetHostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = GetHostSerializer
    filterset_class = HostFilter


# Host Simple
class HostSimpleViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSimpleSerializer


# Host Perm
class HostPermViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSimpleSerializer
    filterset_class = HostFilter

    def list(self, request, *args, **kwargs):
        content_type = request.GET.get('content_type')
        group = request.GET.get('group')
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h.pop('inside_ip')
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

