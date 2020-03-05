from django.forms import ModelChoiceField

from main.forms.base import BaseModelForm
from main.models import Statement, Student


class StatementForm(BaseModelForm):
    student = ModelChoiceField(queryset=Student.objects.select_related('group'))

    class Meta:
        model = Statement
        exclude = ('',)
