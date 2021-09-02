from app.views import AddressViewSet, AccountViewSet, AccountPermViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'accounts-perm', AccountPermViewSet)

urlpatterns = []
