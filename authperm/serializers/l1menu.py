from rest_framework import serializers
from authperm.models import L1Menu


# 一级菜单
class L1MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = L1Menu
        fields = '__all__'
        depth = 1
