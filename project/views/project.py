from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from guardian.models import GroupObjectPermission
from project.models import Project
from project.serializers import ProjectDetailSerializer, ProjectNameSerializer, ProjectSerializer, \
     ProjectListSerializer
from authperm.serializers import GroupObjectPermissionSerializer
from project.filters import ProjectFilter


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.query_params.get('with_perms', False) == 'true':
            return ProjectNameSerializer
        if self.request.query_params.get('retrieve', False) == 'true':
            return ProjectDetailSerializer
        if self.request.method.lower() == 'get':
            return ProjectListSerializer
        return ProjectSerializer

    def get_permissions(self):
        retrieve = self.request.query_params.get('retrieve', 'false')
        if retrieve == 'true':
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def filter_queryset(self, queryset):
        retrieve = self.request.query_params.get('retrieve', 'false')
        if retrieve == 'true':
            self.filter_backends = [DjangoFilterBackend]

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def list(self, request, *args, **kwargs):
        with_perms = request.query_params.get('with_perms', 'false')
        content_type = request.GET.get('content_type')
        group = request.GET.get('group')
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
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # 设置对象权限需要对象权限
        if with_perms == 'true':
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
        return Response(serializer.data)


class ProjectNameViewSet(generics.ListAPIView):
    queryset = Project.objects.filter(used=True)
    serializer_class = ProjectNameSerializer
    pagination_class = None

    def get_permissions(self):
        need_perm = self.request.query_params.get('need_perm', 'true')
        if need_perm == 'false':
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def filter_queryset(self, queryset):
        need_perm = self.request.query_params.get('need_perm', 'true')
        if need_perm == 'false':
            self.filter_backends = [DjangoFilterBackend]

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
