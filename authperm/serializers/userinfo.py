from rest_framework import serializers
from authperm.models import UserInfo
from guardian.models import UserObjectPermission


# 获取单个用户信息
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        depth = 1


# 增删改用户
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'email', 'phone',  'password', 'is_superuser', 'groups', 'user_permissions']


# 查询用户
class GetUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        depth = 3


# 查询用户的主持信息
class GetUserHostedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['username', 'groups', 'hosted', 'hosted_date']
        depth = 1


# 用户对象权限
class UserObjectPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserObjectPermission
        fields = '__all__'
        depth = 1
