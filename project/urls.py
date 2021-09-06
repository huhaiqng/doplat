from django.urls import path
from project.views import GetGaingon666Domain, GetGaingon666DomainRecord, GetLingfannaoDomain, \
    GetLingfannaoDomainRecord, TaskResultViewSet, HostViewSet, EnvViewSet, MySQLViewSet, \
    ConfigViewSet, GetConfigViewSet, ProjectOneViewSet, ProjectNameViewSet, PopularUrlViewSet, \
    MiddlewareViewSet, MiddlewareListViewSet, ProjectViewSet, ProjectListViewSet, \
    ProjectModuleViewSet, ProjectModuleListSet, UrlViewSet, UrlListViewSet, \
    MiddlewarePermViewSet, ProjectPermViewSet, ProjectNameNeedPermViewSet, ProjectModulePermViewSet, UrlPermViewSet, \
    ConfigPermViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'hosts', HostViewSet)
router.register(r'mysql', MySQLViewSet)
router.register(r'config', ConfigViewSet)
router.register(r'config-perm', ConfigPermViewSet)
router.register(r'getConfig', GetConfigViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'project-perm', ProjectPermViewSet)
router.register(r'project-list', ProjectListViewSet)
router.register(r'project-one', ProjectOneViewSet)
router.register(r'project-name', ProjectNameViewSet)
router.register(r'project-name-need-perm', ProjectNameNeedPermViewSet)
router.register(r'popular-url', PopularUrlViewSet)
router.register(r'middleware', MiddlewareViewSet)
router.register(r'middleware-list', MiddlewareListViewSet)
router.register(r'middleware-perm', MiddlewarePermViewSet)
router.register(r'projectmodule', ProjectModuleViewSet)
router.register(r'projectmodule-list', ProjectModuleListSet)
router.register(r'projectmodule-perm', ProjectModulePermViewSet)
router.register(r'url', UrlViewSet)
router.register(r'url-perm', UrlPermViewSet)
router.register(r'url-list', UrlListViewSet)


urlpatterns = [
    path('getGaingon666Domain/', GetGaingon666Domain.as_view()),
    path('getGaingon666DomainRecord/', GetGaingon666DomainRecord.as_view()),
    path('getLingfannaoDomain/', GetLingfannaoDomain.as_view()),
    path('getLingfannaoDomainRecord/', GetLingfannaoDomainRecord.as_view()),
    path('getEnv/', EnvViewSet.as_view()),
    path('taskresult/', TaskResultViewSet.as_view()),
]
