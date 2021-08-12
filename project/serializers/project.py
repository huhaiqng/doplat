from rest_framework import serializers
from .url import UrlSerializer
from .host import ProjectHostSerializer
from .project_module import ProjectModuleSerializer
from project.models import Project, Host
from .env import EnvSerializer
from project.models import Url


class ProjectSerializer(serializers.ModelSerializer):
    urls = UrlSerializer(read_only=True, many=True)
    hosts = ProjectHostSerializer(read_only=True, many=True)
    modules = ProjectModuleSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectForConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class ProjectMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'alias', 'deploy_dir', 'log_dir', 'used']


class GetHostSerializer(serializers.ModelSerializer):
    project = ProjectForConfigSerializer(read_only=True, many=True)

    class Meta:
        model = Host
        fields = '__all__'


class PopularUrlSerializer(serializers.ModelSerializer):
    project = ProjectForConfigSerializer(read_only=True)
    env = EnvSerializer(read_only=True)

    class Meta:
        model = Url
        fields = '__all__'
