import django_filters
from .models import Host, MySQL, Middleware


class HostFilter(django_filters.FilterSet):
    inside_ip = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Host
        fields = ['cloud_user', 'env']


class MySQLFilter(django_filters.FilterSet):
    inside_addr = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = MySQL
        fields = []


class MiddlewareFilter(django_filters.FilterSet):
    conn_addr = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Middleware
        fields = ['env', 'type']
