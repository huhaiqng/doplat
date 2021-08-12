from project.serializers import MySQLSerializer
from project.models import MySQL
from project.filters import MySQLFilter
from rest_framework import viewsets


# MySQL 实例
class MySQLViewSet(viewsets.ModelViewSet):
    queryset = MySQL.objects.all()
    serializer_class = MySQLSerializer
    filterset_class = MySQLFilter
