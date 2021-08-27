from rest_framework import serializers
from project.models import MySQL
from django.contrib.auth.models import Group


# MySQL 实例
class MySQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySQL
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        current_groups = Group.objects.filter(user=current_user)
        # 用户及所在的组
        user_group = [current_user]
        for current_group in current_groups:
            user_group.append(current_group)

        return {
            'view_mysql': user_group,
            'change_mysql': user_group,
            'delete_mysql': user_group
        }
