from django import forms

from general.forms.base import BaseBoostrapFormMixin
from crud.models import Statement


class StatementFormMixin(BaseBoostrapFormMixin, forms.ModelForm):
    class Meta:
        model = Statement
        exclude = ('',)
