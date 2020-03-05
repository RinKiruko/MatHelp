import django_filters

from main.models import StatementCategory


class StatementCategoryFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name='title', lookup_expr='icontains')