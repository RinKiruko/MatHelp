from django.views.generic import FormView

from crud.models import StatementCategory
from distribution.forms import *


class Settings(FormView):
    template_name = "distribution/settings.html"
    form_class = settings_form_factory(StatementCategory.objects.all())
