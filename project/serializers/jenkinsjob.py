from rest_framework import serializers
from project.models import JenkinsJob


class JenkinsJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenkinsJob
        fields = '__all__'


class GetJenkinsJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenkinsJob
        fields = '__all__'
        depth = 1
