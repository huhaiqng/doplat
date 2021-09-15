from rest_framework import serializers
from project.models import GitlabRepo


class GitlabRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitlabRepo
        fields = '__all__'


class GetGitlabRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitlabRepo
        fields = '__all__'
        depth = 1
