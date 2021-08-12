from django.urls import path, include
from project.views import GetGaingon666Domain, GetGaingon666DomainRecord, GetLingfannaoDomain, \
    GetLingfannaoDomainRecord, TaskResultViewSet, HostViewSet, EnvViewSet, MySQLViewSet, AccountViewSet, \
    ConfigViewSet, GetConfigViewSet, ProjectViewSet, ProjectForConfigViewSet, GetHostViewSet, PopularUrlViewSet, \
    ProjectMainViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'taskresult', TaskResultViewSet)
router.register(r'getEnv', EnvViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'getHosts', GetHostViewSet)
router.register(r'mysql', MySQLViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'config', ConfigViewSet)
router.register(r'getConfig', GetConfigViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'project-for-config', ProjectForConfigViewSet)
router.register(r'popular-url', PopularUrlViewSet)
router.register(r'project-main', ProjectMainViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('getGaingon666Domain/', GetGaingon666Domain.as_view()),
    path('getGaingon666DomainRecord/', GetGaingon666DomainRecord.as_view()),
    path('getLingfannaoDomain/', GetLingfannaoDomain.as_view()),
    path('getLingfannaoDomainRecord/', GetLingfannaoDomainRecord.as_view()),
]
