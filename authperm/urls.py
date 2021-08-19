from django.urls import path, include
from authperm.views import UserViewSet, L1MenuViewSet, L2MenuViewSet, GroupViewSet, GetGroupViewSet, \
     GetGroupL2menuView, SetGroupObjectPermsView, UserInfoViewSet, GetUserInfoViewSet, GetUserHostedInfoViewSet, \
     UserObjectPermissionViewSet, GroupObjectPermissionViewSet, GroupNameViewSet, L2MenuContentTypeViewSet, \
     PermissionViewSet, GetLoginUser
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'getL1Menu', L1MenuViewSet)
router.register(r'getL2Menu', L2MenuViewSet)
router.register(r'getL2MenuContentType', L2MenuContentTypeViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'groupsName', GroupNameViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'getGroups', GetGroupViewSet)
router.register(r'userInfo', UserInfoViewSet)
router.register(r'getUserInfo', GetUserInfoViewSet)
router.register(r'getUserHostedInfo', GetUserHostedInfoViewSet)
router.register(r'userObjectPermission', UserObjectPermissionViewSet)
router.register(r'groupObjectPermission', GroupObjectPermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getLoginUser/', GetLoginUser.as_view()),
    path('getGroupL2menu/', GetGroupL2menuView.as_view()),
    path('setGroupObjectPerms/', SetGroupObjectPermsView.as_view()),
]
