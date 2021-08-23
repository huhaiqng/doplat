from rest_framework import serializers
from authperm.models import L1Menu
from .l2menu import L2MenuSerializer


# 增删改
class L1MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = L1Menu
        fields = '__all__'


# List
class L1MenuListSerializer(serializers.ModelSerializer):
    children = L2MenuSerializer(read_only=True, many=True)

    class Meta:
        model = L1Menu
        fields = '__all__'
