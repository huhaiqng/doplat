from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from project.serializers import ProjectDetailSerializer, ProjectNameSerializer, ProjectSerializer, ProjectListSerializer
from project.models import Project
from django_filters.rest_framework import DjangoFilterBackend
from project.filters import ProjectFilter


# 增删改
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter()
    serializer_class = ProjectSerializer


# List
class ProjectListViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(used=True)
    serializer_class = ProjectListSerializer
    filterset_class = ProjectFilter


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
