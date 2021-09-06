from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.hashers import make_password
from authperm.models import UserInfo
from authperm.serializers import UserInfoSerializer, GetUserInfoSerializer, GetUserHostedInfoSerializer, \
    UserPermissionSerializer


class GetLoginUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = UserPermissionSerializer(request.user).data
        return Response(user)


# 增删改用户
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all().order_by('-date_joined')
    filterset_fields = ('groups',)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return GetUserInfoSerializer
        return UserInfoSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class GetUserHostedInfoViewSet(generics.ListAPIView):
    queryset = UserInfo.objects.exclude(
        username__in=['jsb', 'AnonymousUser']).order_by('hosted', 'hosted_date', 'groups', 'date_joined')
    serializer_class = GetUserHostedInfoSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
    pagination_class = None
