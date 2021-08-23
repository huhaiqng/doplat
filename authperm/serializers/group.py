from rest_framework import serializers
from django.contrib.auth.models import Group
from guardian.models import GroupObjectPermission
from authperm.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class GetGroupSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'


# 组对象权限
class GroupObjectPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupObjectPermission
        fields = '__all__'
        depth = 2
