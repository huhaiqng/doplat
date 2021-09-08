from rest_framework import serializers
from authperm.models import UserInfo


# 获取用户权限
class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'is_superuser', 'groups', 'user_permissions']
        depth = 2


# 增删改用户
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'real_name', 'phone', 'email', 'password', 'is_superuser', 'groups']


# 查询用户
class GetUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        # fields = '__all__'
        fields = ['id', 'username', 'real_name', 'phone', 'email', 'password', 'is_superuser', 'hosted', 'groups',
                  'date_joined']
        depth = 1


# 查询用户的主持信息
class GetUserHostedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['username', 'groups', 'hosted', 'hosted_date']
        depth = 1


# 查询用户的主持信息
class UserSimpledInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username']
        depth = 1
