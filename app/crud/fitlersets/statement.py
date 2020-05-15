import django_filters
from django.db.models import QuerySet, Q

from crud.models import StatementCategory


class StatementFilter(django_filters.FilterSet):
    group = django_filters.CharFilter(field_name='student_group', lookup_expr='icontains')
    student = django_filters.CharFilter(method='filter_text')
    category = django_filters.ModelChoiceFilter(field_name='statement_category',
                                                queryset=StatementCategory.objects.all())

    def filter_text(self, queryset: QuerySet, _, value):
        return queryset.filter(
            Q(student_first_name__icontains=value) | Q(student_last_name__icontains=value)
        )
