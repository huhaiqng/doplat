from django.urls import path, include
from authperm.views import UserViewSet, L1MenuListViewSet, L2MenuViewSet, GroupViewSet, GetGroupViewSet, \
     GetGroupL2menuView, SetGroupObjectPermsView, UserInfoViewSet, GetUserInfoViewSet, GetUserHostedInfoViewSet, \
     UserObjectPermissionViewSet, GroupObjectPermissionViewSet, GroupNameViewSet, L2MenuContentTypeViewSet, \
     PermissionViewSet, GetLoginUser, L1MenuViewSet, L2MenuListViewSet, ContentTypeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'l1menu', L1MenuViewSet)
router.register(r'l1menu-list', L1MenuListViewSet)
router.register(r'l2menu', L2MenuViewSet)
router.register(r'l2menu-list', L2MenuListViewSet)
router.register(r'getL2MenuContentType', L2MenuContentTypeViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'getGroups', GetGroupViewSet)
router.register(r'group-name', GroupNameViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'userInfo', UserInfoViewSet)
router.register(r'getUserInfo', GetUserInfoViewSet)
router.register(r'getUserHostedInfo', GetUserHostedInfoViewSet)
router.register(r'userObjectPermission', UserObjectPermissionViewSet)
router.register(r'groupobjectpermission', GroupObjectPermissionViewSet)
router.register(r'contenttype', ContentTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getLoginUser/', GetLoginUser.as_view()),
    path('getGroupL2menu/', GetGroupL2menuView.as_view()),
    path('setGroupObjectPerms/', SetGroupObjectPermsView.as_view())
]
