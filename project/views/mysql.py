from project.serializers import MySQLSerializer
from project.models import MySQL
from project.filters import MySQLFilter
from rest_framework import viewsets
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupObjectPermissionSerializer


# MySQL 实例
class MySQLViewSet(viewsets.ModelViewSet):
    queryset = MySQL.objects.all()
    serializer_class = MySQLSerializer
    filterset_class = MySQLFilter


# MySQL Perm
class MySQLPermViewSet(viewsets.ModelViewSet):
    queryset = MySQL.objects.all()
    serializer_class = MySQLSerializer
    filterset_class = MySQLFilter

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
                h['name'] = h.pop('inside_addr')
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
