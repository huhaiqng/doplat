from rest_framework import serializers
from project.models import Config
from .project import ProjectNameSerializer
from .env import EnvSerializer
from django.contrib.auth.models import Group


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        current_groups = Group.objects.filter(user=current_user)
        # 用户及所在的组
        user_group = [current_user]
        for current_group in current_groups:
            user_group.append(current_group)

        return {
            'change_config': user_group,
            'delete_config': user_group,
            'view_config': user_group
        }


class GetConfigSerializer(serializers.ModelSerializer):
    env = EnvSerializer(read_only=True)
    project = ProjectNameSerializer(read_only=True)

    class Meta:
        model = Config
        fields = '__all__'
