from django import forms

from general.forms.base import BaseBoostrapFormMixin
from crud.models import StatementCategory


class StatementCategoryFormMixin(BaseBoostrapFormMixin, forms.ModelForm):
    class Meta:
        model = StatementCategory
        exclude = ('',)
