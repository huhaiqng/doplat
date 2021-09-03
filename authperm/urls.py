from django.urls import path
from authperm.views import L2MenuViewSet, GroupViewSet, GetGroupViewSet, UserInfoViewSet, \
     GetUserHostedInfoViewSet, GroupObjectPermissionViewSet, GroupNameViewSet, L2MenuContentTypeViewSet, \
     PermissionViewSet, GetLoginUser, L1MenuViewSet, ContentTypeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'l1menu', L1MenuViewSet)
router.register(r'l2menu', L2MenuViewSet)
# router.register(r'getL2MenuContentType', L2MenuContentTypeViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'getGroups', GetGroupViewSet)
router.register(r'group-name', GroupNameViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'userinfo', UserInfoViewSet)
router.register(r'contenttype', ContentTypeViewSet)
router.register(r'groupobjectpermission', GroupObjectPermissionViewSet)

urlpatterns = [
    path('getLoginUser/', GetLoginUser.as_view()),
    path('getUserHostedInfo/', GetUserHostedInfoViewSet.as_view()),
    path('getL2MenuContentType/', L2MenuContentTypeViewSet.as_view())
]
