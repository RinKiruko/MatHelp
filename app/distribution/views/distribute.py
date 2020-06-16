import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q, Prefetch
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import View

from crud.models import Statement, StatementCategory
from distribution.utils import get_criterion, normalize


class Distribute(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        budget = int(request.GET['budget'])
        date = timezone.datetime(kwargs['year'], kwargs['month'], 1).date()

        categories = StatementCategory.objects.filter(
            statements__application_date__year=date.year,
            statements__application_date__month=date.month
        ).annotate(
            statements_count=Count(
                'statements',
                filter=(
                        Q(statements__application_date__year=date.year) &
                        Q(statements__application_date__month=date.month)
                )
            )
        ).prefetch_related(
            Prefetch(
                'statements',
                queryset=Statement.objects.filter(application_date__year=date.year, application_date__month=date.month)
            )
        )

        test_metrics = {
            category: {
                'count': normalize(
                    category.statements_count,
                    [category.statements_count for category in categories]
                ),
                'weight': normalize(
                    category.weight,
                    [category.weight for category in categories]
                )
            } for category in categories
        }

        estimated = {
            category: get_criterion(test_metrics[category])
            for category in categories
        }

        distribution = {
            category: budget * (estimated[category] / sum(estimated.values())) for category in categories
        }

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="distribution{date.year}{date.year}.csv"'

        writer = csv.writer(response)
        for category, category_budget in distribution.items():
            writer.writerows([
                [statement.student_data, category.title, "{:.2f}".format(category_budget / category.statements_count)]
                for statement in category.statements.all()
            ])

        return response
