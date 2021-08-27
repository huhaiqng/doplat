from rest_framework import serializers
from django.contrib.auth.models import Group
from guardian.models import GroupObjectPermission
from authperm.serializers import UserSimpledInfoSerializer


# 增删改
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']


# List
class GetGroupSerializer(serializers.ModelSerializer):
    user_set = UserSimpledInfoSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'
        depth = 1


class GroupNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


# 组对象权限
class GroupObjectPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupObjectPermission
        fields = '__all__'
        depth = 2
