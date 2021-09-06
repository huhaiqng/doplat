from django.urls import path
from authperm.views import L2MenuViewSet, GroupViewSet, UserInfoViewSet, \
     GetUserHostedInfoViewSet, GroupObjectPermissionViewSet, L2MenuContentTypeViewSet, \
     PermissionViewSet, GetLoginUser, L1MenuViewSet, ContentTypeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'userinfo', UserInfoViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'groupobjectpermission', GroupObjectPermissionViewSet)
router.register(r'l1menu', L1MenuViewSet)
router.register(r'l2menu', L2MenuViewSet)

urlpatterns = [
    path('getLoginUser/', GetLoginUser.as_view()),
    path('getUserHostedInfo/', GetUserHostedInfoViewSet.as_view()),
    path('getL2MenuContentType/', L2MenuContentTypeViewSet.as_view()),
    path('permission/', PermissionViewSet.as_view()),
    path('contenttype/', ContentTypeViewSet.as_view())
]
