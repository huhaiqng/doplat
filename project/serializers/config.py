from rest_framework import serializers
from project.models import Config
from .project import ProjectNameSerializer
from .env import EnvSerializer


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'


class GetConfigSerializer(serializers.ModelSerializer):
    env = EnvSerializer(read_only=True)
    project = ProjectNameSerializer(read_only=True)

    class Meta:
        model = Config
        fields = '__all__'
