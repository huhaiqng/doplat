from django.urls import path, include
from app.views import AddressViewSet, AccountViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
