from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from guardian.models import GroupObjectPermission
from project.models import Url
from project.serializers import PopularUrlSerializer, UrlSerializer, UrlListSerializer
from authperm.serializers import GroupObjectPermissionSerializer


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    filterset_fields = ('project',)

    def get_queryset(self):
        with_perms = self.request.query_params.get('with_perms', 'false')
        name = self.request.query_params.get('name', '')
        if with_perms == 'true':
            queryset = Url.objects.filter(project__name__icontains=name)
        else:
            queryset = Url.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return UrlListSerializer
        return UrlSerializer

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
                    h['name'] = h['project']['name'] + '  ' + h.pop('name') + ':  ' + h['url']
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # 设置对象权限需要对象权限
        if with_perms == 'true':
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h['project']['name'] + '  ' + h.pop('name') + ':  ' + h['url']
        return Response(serializer.data)


class PopularUrlViewSet(generics.ListAPIView):
    queryset = Url.objects.filter(popular=True).order_by('project__name', 'env__name', 'name')
    serializer_class = PopularUrlSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
    pagination_class = None
