from rest_framework import serializers
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin
from django.contrib.auth.models import Group
from project.models import Middleware
from .project import ProjectNameSerializer


# 增删改
class MiddlewareSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Middleware
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        current_groups = Group.objects.filter(user=current_user)
        # 用户及所在的组
        user_group = [current_user]
        for current_group in current_groups:
            user_group.append(current_group)

        return {
            'view_middleware': user_group,
            'change_middleware': user_group,
            'delete_middleware': user_group
        }


# 列表
class MiddlewareListSerializer(serializers.ModelSerializer):
    project = ProjectNameSerializer(read_only=True, many=True)

    class Meta:
        model = Middleware
        fields = '__all__'
        depth = 1
