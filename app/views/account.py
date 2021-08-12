from app.models import Account
from app.serializers import AccountSerializer
from app.filters import AccountFilter
from rest_framework import viewsets


# 用户
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filterset_class = AccountFilter
