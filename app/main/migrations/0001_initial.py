# Generated by Django 3.0.3 on 2020-04-16 09:30

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import main.models.mixins.template_model_meta


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StatementCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название категории')),
                ('legal_number', models.CharField(max_length=50, verbose_name='Юридический номер')),
                ('maximum_payment', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Максимальная выплата')),
                ('weight', models.FloatField(verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Категория заявления',
                'verbose_name_plural': 'Категории заявлений',
            },
            bases=(main.models.mixins.template_model_meta.TemplateModelMetaInfoMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_payment', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Запрашиваемая сумма')),
                ('student_first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('student_last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('student_middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('student_group', models.CharField(max_length=50, verbose_name='Группа')),
                ('statement_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statements', to='main.StatementCategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Заявление',
                'verbose_name_plural': 'Заявления',
            },
            bases=(main.models.mixins.template_model_meta.TemplateModelMetaInfoMixin, models.Model),
        ),
    ]