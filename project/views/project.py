from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from project.serializers import ProjectSerializer, ProjectForConfigSerializer, ProjectMainSerializer
from project.models import Project
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(used=True)
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]


class ProjectForConfigViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(used=True)
    serializer_class = ProjectForConfigSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]


class ProjectMainViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectMainSerializer
    permission_classes = [AllowAny]

    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        PageNumberPagination.page_size = page_size

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        PageNumberPagination.page_size = None

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
