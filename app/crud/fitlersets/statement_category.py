import django_filters
from django.db.models import Q


class StatementCategoryFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='text_filtering')

    @staticmethod
    def text_filtering(queryset, _, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(legal_number__iexact=value)
        )