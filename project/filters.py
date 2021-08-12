import django_filters
from .models import Host, MySQL


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

