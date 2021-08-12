from django.urls import path, include
from app.views import AddressViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
