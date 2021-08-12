from rest_framework import serializers
from project.models import MySQL


# MySQL 实例
class MySQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySQL
        fields = '__all__'
