from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from guardian.models import UserObjectPermission
from authperm.models import UserInfo
from authperm.serializers import UserSerializer, UserInfoSerializer, GetUserInfoSerializer, \
    GetUserHostedInfoSerializer, UserObjectPermissionSerializer, UserPermissionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.hashers import make_password


# 用户信息
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('username',)


# 用户信息
class UserPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserPermissionSerializer
    filterset_fields = ('username',)


# 增删改用户
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all().order_by('-date_joined')
    serializer_class = UserInfoSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        print(request.data['password'])
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


# 查询用户
class GetUserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all().order_by('date_joined')
    serializer_class = GetUserInfoSerializer
    filterset_fields = ('groups',)


# 查询用户主持
class GetUserHostedInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.exclude(
        username__in=['jsb', 'AnonymousUser']).order_by('hosted', 'hosted_date', 'groups', 'date_joined')
    serializer_class = GetUserHostedInfoSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]


# 用户对象权限
class UserObjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserObjectPermission.objects.all()
    serializer_class = UserObjectPermissionSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
