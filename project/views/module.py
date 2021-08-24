from project.serializers import ProjectModuleSerializer, ProjectModuleListSerializer
from project.models import ProjectModule
from rest_framework import viewsets


class ProjectModuleViewSet(viewsets.ModelViewSet):
    queryset = ProjectModule.objects.all()
    serializer_class = ProjectModuleSerializer


class ProjectModuleListSet(viewsets.ModelViewSet):
    queryset = ProjectModule.objects.all()
    serializer_class = ProjectModuleListSerializer
    filterset_fields = ('project',)
