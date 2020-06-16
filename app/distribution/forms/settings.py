from django import forms
from django.db.models import QuerySet

from general.forms import *


def settings_form_factory(categories: QuerySet):
    fields = {
        'budget': forms.DecimalField(required=True, min_value=0),
        'distribution_period': forms.DateField(required=True)
    }

    fields.update({
        f'{category.id}': forms.BooleanField(required=True) for category in categories
    })

    result = type(
        'SettingsForm',
        (BaseBoostrapForm,),
        fields
    )

    return result
