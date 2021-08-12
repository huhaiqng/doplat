import django_filters
from .models import Host, MySQL, Account


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


class AccountFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Account
        fields = []
