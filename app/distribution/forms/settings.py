from django import forms
from django.db.models import QuerySet
from django.utils import timezone

from crud.models import StatementCategory, Statement
from general.forms import *

MONTH_CHOICES = (
    (1, 'Январь'),
    (2, 'Февраль'),
    (3, 'Март'),
    (4, 'Апрель'),
    (5, 'Май'),
    (6, 'Июнь'),
    (7, 'Июль'),
    (8, 'Август'),
    (9, 'Сентябрь'),
    (10, 'Октябрь'),
    (11, 'Ноябрь'),
    (12, 'Декбрь'),
)


class SettingsValidationMixin:
    def clean(self):
        cleaned_data = super().clean()

        if any(cleaned_data.get(cat.id, False) for cat in StatementCategory.objects.all()):
            raise forms.ValidationError("Хотя бы одна категория должна быть выбрана")

        return cleaned_data


def settings_form_factory(categories: QuerySet = StatementCategory.objects.all()):
    today = timezone.now().date()

    fields = {
        'budget': forms.FloatField(required=True, label='Размер бюджета', min_value=1000),
        'distribution_year': forms.IntegerField(
            required=True,
            label='Год',
            initial=today.year,
        ),
        'distribution_month': forms.TypedChoiceField(
            required=True,
            label='Месяц',
            coerce=int,
            empty_value=1,
            choices=MONTH_CHOICES
        )
    }
    fields.update({
        str(category.id): forms.BooleanField(
            label=category,
            initial=True,
            required=False,
        ) for category in categories
    })

    result = type(
        'SettingsForm',
        (SettingsValidationMixin, BaseBoostrapFormMixin, forms.Form),
        fields
    )

    return result
