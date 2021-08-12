from project.models import Account
from project.serializers import AccountSerializer
from project.filters import AccountFilter
from rest_framework import viewsets


# 用户
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filterset_class = AccountFilter
