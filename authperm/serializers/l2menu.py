from rest_framework import serializers
from authperm.models import L2Menu


# 二级菜单
class L2MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Menu
        fields = '__all__'


class L2MenuContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Menu
        fields = ['title', 'content_type']
        depth = 1
