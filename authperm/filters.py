import django_filters
from .models import L1Menu, L2Menu
from guardian.models import GroupObjectPermission


class L1MenuFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = L1Menu
        fields = []


class L2MenuFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = L2Menu
        fields = []
