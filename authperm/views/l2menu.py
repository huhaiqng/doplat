from rest_framework import viewsets, generics
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from django.contrib.auth.models import Permission
from authperm.models import L2Menu
from authperm.serializers import L2MenuSerializer, L2MenuContentTypeSerializer, L2MenuListSerializer
from authperm.serializers import GroupObjectPermissionSerializer
from authperm.serializers import PermissionSerializer
from authperm.filters import L2MenuFilter


class L2MenuViewSet(viewsets.ModelViewSet):
    queryset = L2Menu.objects.all()
    filterset_class = L2MenuFilter

    def get_serializer_class(self):
        if self.request.query_params.get('paged', True) == 'false':
            return L2MenuSerializer
        if self.request.method.lower() == 'get':
            return L2MenuListSerializer

        return L2MenuSerializer

    def list(self, request, *args, **kwargs):
        with_perms = request.query_params.get('with_perms', 'false')
        content_type = request.query_params.get('content_type', None)
        group = request.query_params.get('group', None)

        if request.query_params.get('paged', True) == 'false':
            self.pagination_class = None
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # 设置对象权限需要对象权限
            if with_perms == 'true':
                for h in serializer.data:
                    perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type,
                                                                 group=group)
                    h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                    h['perms'] = perms.values_list('permission', flat=True)
                    h['name'] = h['parent']['title'] + '->' + h.pop('title')
                return self.get_paginated_response(serializer.data)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # 设置对象权限需要对象权限
        if with_perms == 'true':
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type,
                                                             group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h['parent']['title'] + '->' + h.pop('title')
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


class L2MenuContentTypeViewSet(generics.ListAPIView):
    queryset = L2Menu.objects.filter(content_type__isnull=False)
    serializer_class = L2MenuContentTypeSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        for lc in serializer.data:
            perms = Permission.objects.filter(content_type_id=lc['content_type']['id'])
            lc['perms'] = PermissionSerializer(perms, many=True).data
        return Response(serializer.data)
