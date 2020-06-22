import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q, Prefetch
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from crud.models import Statement, StatementCategory
from distribution.forms import settings_form_factory
from distribution.utils import get_criterion, normalize


class Distribute(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form_class = settings_form_factory()
        form = form_class(data=request.GET)
        if not form.is_valid():
            return render(request, 'distribution/settings.html', {'form': form})

        distribution_year = form.cleaned_data.pop('distribution_year')
        distribution_month = form.cleaned_data.pop('distribution_month')
        budget = form.cleaned_data.pop('budget')

        categories = StatementCategory.objects.filter(
            statements__application_date__year=distribution_year,
            statements__application_date__month=distribution_month
        ).annotate(
            statements_count=Count(
                'statements',
                filter=(
                        Q(statements__application_date__year=distribution_year) &
                        Q(statements__application_date__month=distribution_month)
                )
            )
        ).prefetch_related(
            Prefetch(
                'statements',
                queryset=Statement.objects.filter(application_date__year=distribution_year,
                                                  application_date__month=distribution_month)
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
        response['Content-Disposition'] = 'attachment; filename="distribution{}{}.csv"'.format(distribution_year,
                                                                                               distribution_month)

        writer = csv.writer(response)
        for category, category_budget in distribution.items():
            writer.writerows([
                [statement.student_data, category.title, "{:.2f}".format(category_budget / category.statements_count)]
                for statement in category.statements.all()
            ])

        return response
