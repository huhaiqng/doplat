from rest_framework import serializers
from project.models import Url


# 增删改
class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'


# List
class UrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'
        depth = 1
