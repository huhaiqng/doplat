from django.urls import path
from project.views import GetGaingon666Domain, GetGaingon666DomainRecord, GetLingfannaoDomain, GitlabRepoViewSet, \
    GetLingfannaoDomainRecord, TaskResultViewSet, HostViewSet, EnvViewSet, MySQLViewSet, ConfigViewSet, \
    ProjectNameViewSet, PopularUrlViewSet, MiddlewareViewSet, ProjectViewSet, ProjectModuleViewSet, UrlViewSet, \
    JenkinsJobViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'hosts', HostViewSet)
router.register(r'mysql', MySQLViewSet)
router.register(r'config', ConfigViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'middleware', MiddlewareViewSet)
router.register(r'projectmodule', ProjectModuleViewSet)
router.register(r'url', UrlViewSet)
router.register(r'jenkinsjob', JenkinsJobViewSet)
router.register(r'gitlabrepo', GitlabRepoViewSet)


urlpatterns = [
    path('getGaingon666Domain/', GetGaingon666Domain.as_view()),
    path('getGaingon666DomainRecord/', GetGaingon666DomainRecord.as_view()),
    path('getLingfannaoDomain/', GetLingfannaoDomain.as_view()),
    path('getLingfannaoDomainRecord/', GetLingfannaoDomainRecord.as_view()),
    path('getEnv/', EnvViewSet.as_view()),
    path('taskresult/', TaskResultViewSet.as_view()),
    path('popular-url/', PopularUrlViewSet.as_view()),
    path('project-name/', ProjectNameViewSet.as_view()),
]
