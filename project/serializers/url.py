from rest_framework import serializers
from .env import EnvSerializer
from project.models import Url


class UrlSerializer(serializers.ModelSerializer):
    env = EnvSerializer(read_only=True)

    class Meta:
        model = Url
        fields = '__all__'
