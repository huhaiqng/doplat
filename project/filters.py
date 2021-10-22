import django_filters
from .models import Host, MySQL, Middleware, Project, JenkinsJob, GitlabRepo


class HostFilter(django_filters.FilterSet):
    inside_ip = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Host
        fields = ['cloud_user', 'env']


class MySQLFilter(django_filters.FilterSet):
    inside_addr = django_filters.CharFilter(lookup_expr='icontains')
    project = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = MySQL
        fields = []


class MiddlewareFilter(django_filters.FilterSet):
    conn_addr = django_filters.CharFilter(lookup_expr='icontains')
    project = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Middleware
        fields = ['env', 'type']


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Project
        fields = []


class JenkinsJobFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = JenkinsJob
        fields = ['project']


class GitlabRepoFilter(django_filters.FilterSet):
    path_with_namespace = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = GitlabRepo
        fields = ['project']
