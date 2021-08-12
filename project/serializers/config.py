from rest_framework import serializers
from project.models import Config
from .project import ProjectForConfigSerializer
from .env import EnvSerializer


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'


class GetConfigSerializer(serializers.ModelSerializer):
    env = EnvSerializer(read_only=True)
    project = ProjectForConfigSerializer(read_only=True)

    class Meta:
        model = Config
        fields = '__all__'
