from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from project.serializers import ProjectDetailSerializer, ProjectNameSerializer, ProjectSerializer, \
    ProjectListSerializer, ProjectNameNeedPermSerializer
from project.models import Project
from django_filters.rest_framework import DjangoFilterBackend
from project.filters import ProjectFilter
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupObjectPermissionSerializer


# 增删改
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return ProjectListSerializer
        return ProjectSerializer


class ProjectOneViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(used=True)
    serializer_class = ProjectDetailSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]


class ProjectNameViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(used=True)
    serializer_class = ProjectNameSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
    pagination_class = None


class ProjectNameNeedPermViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(used=True)
    serializer_class = ProjectNameNeedPermSerializer
    pagination_class = None


class ProjectPermViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(used=True)
    serializer_class = ProjectNameSerializer
    filterset_class = ProjectFilter

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
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
