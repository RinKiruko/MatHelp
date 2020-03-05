from django.forms import ModelChoiceField

from main.forms.base import BaseModelForm
from main.models import Group, Student


class GroupForm(BaseModelForm):
    chief = ModelChoiceField(label='Староста', queryset=Student.objects.select_related('group'))

    class Meta:
        model = Group
        exclude = ('',)
