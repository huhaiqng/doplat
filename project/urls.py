from django.urls import path, include
from project.views import GetGaingon666Domain, GetGaingon666DomainRecord, GetLingfannaoDomain, \
    GetLingfannaoDomainRecord, TaskResultViewSet, HostViewSet, EnvViewSet, MySQLViewSet, \
    ConfigViewSet, GetConfigViewSet, ProjectOneViewSet, ProjectNameViewSet, GetHostViewSet, PopularUrlViewSet, \
    MiddlewareViewSet, MiddlewareListViewSet, ProjectViewSet, ProjectListViewSet, HostSimpleViewSet, \
    ProjectModuleViewSet, ProjectModuleListSet, UrlViewSet, UrlListViewSet, HostPermViewSet, MySQLPermViewSet, \
    MiddlewarePermViewSet, ProjectPermViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'taskresult', TaskResultViewSet)
router.register(r'getEnv', EnvViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'hosts-simple', HostSimpleViewSet)
router.register(r'getHosts', GetHostViewSet)
router.register(r'host-perm', HostPermViewSet)
router.register(r'mysql', MySQLViewSet)
router.register(r'mysql-perm', MySQLPermViewSet)
router.register(r'config', ConfigViewSet)
router.register(r'getConfig', GetConfigViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'project-perm', ProjectPermViewSet)
router.register(r'project-list', ProjectListViewSet)
router.register(r'project-one', ProjectOneViewSet)
router.register(r'project-name', ProjectNameViewSet)
router.register(r'popular-url', PopularUrlViewSet)
router.register(r'middleware', MiddlewareViewSet)
router.register(r'middleware-list', MiddlewareListViewSet)
router.register(r'middleware-perm', MiddlewarePermViewSet)
router.register(r'projectmodule', ProjectModuleViewSet)
router.register(r'projectmodule-list', ProjectModuleListSet)
router.register(r'url', UrlViewSet)
router.register(r'url-list', UrlListViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('getGaingon666Domain/', GetGaingon666Domain.as_view()),
    path('getGaingon666DomainRecord/', GetGaingon666DomainRecord.as_view()),
    path('getLingfannaoDomain/', GetLingfannaoDomain.as_view()),
    path('getLingfannaoDomainRecord/', GetLingfannaoDomainRecord.as_view()),
]
