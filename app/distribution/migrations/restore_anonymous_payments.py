import os
import pickle
from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import migrations


def restore_anonymous_payments(apps, schema_editor):
    # Check file existing
    if not os.path.exists(settings.INITIAL_DATASETS_PATH):
        raise ImproperlyConfigured('There is no initial dataset file')

    StatementCategory = apps.get_model('crud', 'StatementCategory')
    Payment = apps.get_model('distribution', 'Payment')

    dataset = pickle.load(open(settings.INITIAL_DATASETS_PATH, 'rb'))

    payments = []
    for category, payment_date, amount in dataset:
        try:
            category = StatementCategory.objects.get(legal_number__iexact=category)
        except StatementCategory.DoesNotExist:
            category = StatementCategory.objects.create(title=category, legal_number=category)
            category.save()
        except StatementCategory.MultipleObjectsReturned:
            category = StatementCategory.objects.filter(legal_number__iexact=category).first()

        payments += [
            Payment(
                amount=Decimal(amount),
                date=payment_date,
                statement_category=category,
                statement=None
            )
        ]
    
    Payment.objects.bulk_create(payments)


class Migration(migrations.Migration):
    dependencies = [
        ('distribution', '0001_auto_20200515_1520'),
    ]

    operations = [
        migrations.RunPython(restore_anonymous_payments),
    ]
