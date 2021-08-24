from rest_framework import serializers
from .url import UrlListSerializer
from .host import HostSimpleSerializer
from .module import ProjectModuleSerializer
from project.models import Project, Host
from .env import EnvSerializer
from project.models import Url


# 增删改
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


# List
class ProjectListSerializer(serializers.ModelSerializer):
    hosts = HostSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectDetailSerializer(serializers.ModelSerializer):
    urls = UrlListSerializer(read_only=True, many=True)
    hosts = HostSimpleSerializer(read_only=True, many=True)
    modules = ProjectModuleSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class GetHostSerializer(serializers.ModelSerializer):
    project = ProjectNameSerializer(read_only=True, many=True)

    class Meta:
        model = Host
        fields = '__all__'


class PopularUrlSerializer(serializers.ModelSerializer):
    project = ProjectNameSerializer(read_only=True)
    env = EnvSerializer(read_only=True)

    class Meta:
        model = Url
        fields = '__all__'
