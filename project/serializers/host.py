from rest_framework import serializers
from project.models import Host
from django.contrib.auth.models import Group
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin


class HostSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        current_groups = Group.objects.filter(user=current_user)
        user_group = [current_user]
        for current_group in current_groups:
            user_group.append(current_group)

        return {
            'view_host': user_group,
            'change_host': user_group,
            'delete_host': user_group
        }


class ProjectHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['id', 'name', 'hostname', 'inside_ip', 'env']
