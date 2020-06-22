from django.utils import timezone
from django.views.generic import FormView

from crud.models import StatementCategory
from distribution.forms import *


class Settings(FormView):
    template_name = "distribution/settings.html"

    def get_form_class(self):
        return settings_form_factory()

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            'distribution_period': timezone.now().date(),
            'budget': 0,
        })
        initial.update({
            str(category.id): 'true' for category in StatementCategory.objects.all()
        })

        return initial
