from rest_framework import serializers
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin
from django.contrib.auth.models import Group
from app.models import Account


class AccountSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        current_groups = Group.objects.filter(user=current_user)
        # 用户及所在的组
        user_group = [current_user]
        for current_group in current_groups:
            user_group.append(current_group)

        return {
            'view_account': user_group,
            'change_account': user_group,
            'delete_account': user_group
        }
