from rest_framework import serializers
from project.models import ProjectModule


class ProjectModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectModule
        fields = '__all__'
