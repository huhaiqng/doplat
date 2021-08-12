import django_filters
from .models import Account


class AccountFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Account
        fields = []
