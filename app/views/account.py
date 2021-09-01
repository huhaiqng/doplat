from app.models import Account
from app.serializers import AccountSerializer
from app.filters import AccountFilter
from rest_framework import viewsets
from rest_framework.response import Response
from guardian.models import GroupObjectPermission
from authperm.serializers import GroupObjectPermissionSerializer


# 用户
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filterset_class = AccountFilter


# Account Perm
class AccountPermViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filterset_class = AccountFilter

    def list(self, request, *args, **kwargs):
        content_type = request.GET.get('content_type')
        group = request.GET.get('group')
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for h in serializer.data:
                perms = GroupObjectPermission.objects.filter(object_pk=h['id'], content_type=content_type, group=group)
                h['perms_detail'] = GroupObjectPermissionSerializer(perms, many=True).data
                h['perms'] = perms.values_list('permission', flat=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
