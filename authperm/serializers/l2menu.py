from rest_framework import serializers
from authperm.models import L2Menu


# 增删改
class L2MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Menu
        fields = '__all__'


# List
class L2MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Menu
        fields = '__all__'
        depth = 1


class L2MenuContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Menu
        fields = ['id', 'title', 'content_type']
        depth = 1
