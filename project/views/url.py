from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from project.serializers import PopularUrlSerializer, UrlSerializer, UrlListSerializer
from project.models import Url
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupObjectPermissionSerializer


# 增删改
class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


# List
class UrlListViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlListSerializer
    filterset_fields = ('project',)


class PopularUrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.filter(popular=True).order_by('project__name', 'env__name', 'name')
    serializer_class = PopularUrlSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
    pagination_class = None


# Url Perm
class UrlPermViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlListSerializer

    def list(self, request, *args, **kwargs):
        content_type = request.GET.get('content_type')
        group = request.GET.get('group')
        name = request.GET.get('name')
        queryset = Url.objects.filter(project__name__icontains=name)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
                h['name'] = h['project']['name'] + '  ' + h.pop('name') + ':  ' + h['url']
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
