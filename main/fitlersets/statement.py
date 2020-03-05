import django_filters

from main.models import Group, StatementCategory


class StatementFilter(django_filters.FilterSet):
    group = django_filters.ModelChoiceFilter(field_name='student__group', queryset=Group.objects.all())
    study_level = django_filters.CharFilter(field_name='student__group__studying_level')
    category = django_filters.ModelChoiceFilter(field_name='statement_category',
                                                queryset=StatementCategory.objects.all())
