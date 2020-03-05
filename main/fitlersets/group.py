import django_filters

from main.models import Group


class GroupFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    course = django_filters.NumberFilter(field_name='course')

    class Meta:
        model = Group
        fields = ('course', 'studying_level')
