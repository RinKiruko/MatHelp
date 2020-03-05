from django import forms

from main.forms.base import BaseModelForm
from main.models import Group
from main.models import Student


class StudentForm(BaseModelForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        label='Группа',
        widget=forms.Select(attrs={'class': 'form-control'}))

    error_css_class = 'is-invalid'

    class Meta:
        model = Student
        exclude = ('sorting_weight',)
