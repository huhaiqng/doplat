from rest_framework import serializers
from project.models import ProjectModule


# 增删改
class ProjectModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModule
        fields = '__all__'


# 增删改
class ProjectModuleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModule
        fields = '__all__'
        depth = 1
