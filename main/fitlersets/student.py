import django_filters
from django.db.models import QuerySet, Q

from main.models import Student


class StudentFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='filter_text')
    study_level = django_filters.CharFilter(field_name='group__studying_level')
    course = django_filters.CharFilter(field_name='group__course')

    class Meta:
        model = Student
        fields = ['group', ]

    def filter_text(self, queryset: QuerySet, _, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(student_card_id__icontains=value)
        )
