from rest_framework import serializers
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin
from django.contrib.auth.models import Group
from project.models import Project, Host
from project.models import Url
from .url import UrlListSerializer
from .host import HostSimpleSerializer
from .module import ProjectModuleSerializer
from .env import EnvSerializer
from .jenkinsjob import GetJenkinsJobSerializer
from .gitlabrepo import GitlabRepoSerializer


# 增删改
class ProjectSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        current_groups = Group.objects.filter(user=current_user)
        # 用户及所在的组
        user_group = [current_user]
        for current_group in current_groups:
            user_group.append(current_group)

        return {
            'view_project': user_group,
            'change_project': user_group,
            'delete_project': user_group
        }


# List
class ProjectListSerializer(serializers.ModelSerializer):
    hosts = HostSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectDetailSerializer(serializers.ModelSerializer):
    urls = UrlListSerializer(read_only=True, many=True)
    hosts = HostSimpleSerializer(read_only=True, many=True)
    modules = ProjectModuleSerializer(read_only=True, many=True)
    jenkinsjobs = GetJenkinsJobSerializer(read_only=True, many=True)
    gitlabrepos = GitlabRepoSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class GetHostSerializer(serializers.ModelSerializer):
    project = ProjectNameSerializer(read_only=True, many=True)

    class Meta:
        model = Host
        fields = '__all__'


class PopularUrlSerializer(serializers.ModelSerializer):
    project = ProjectNameSerializer(read_only=True)
    env = EnvSerializer(read_only=True)

    class Meta:
        model = Url
        fields = '__all__'
