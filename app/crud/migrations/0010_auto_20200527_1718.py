# Generated by Django 3.0.3 on 2020-05-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_auto_20200525_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='application_date',
            field=models.DateField(verbose_name='Дата Подачи'),
        ),
    ]