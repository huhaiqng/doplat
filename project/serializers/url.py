from rest_framework import serializers
from project.models import Url
from django.contrib.auth.models import Group


# 增删改
class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        current_groups = Group.objects.filter(user=current_user)
        # 用户及所在的组
        user_group = [current_user]
        for current_group in current_groups:
            user_group.append(current_group)

        return {
            'view_url': user_group,
            'change_url': user_group,
            'delete_url': user_group
        }


# List
class UrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'
        depth = 1
