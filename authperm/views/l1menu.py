from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from authperm.models import L1Menu
from authperm.serializers import L1MenuSerializer, L1MenuListSerializer
from authperm.filters import L1MenuFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


# 增删改
class L1MenuViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuSerializer


# List
class L1MenuListViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuListSerializer
    filterset_class = L1MenuFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if request.query_params.get('paged', True) == 'false':
            self.pagination_class = None
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
