from django.db import models
from django.urls import reverse
from django.utils import timezone

from crud.models.mixins import TemplateModelMetaInfoMixin


class Statement(TemplateModelMetaInfoMixin, models.Model):
    requested_payment = models.DecimalField(verbose_name='Запрашиваемая сумма', max_digits=7, decimal_places=2)

    statement_category = models.ForeignKey('crud.StatementCategory', related_name='statements',
                                           on_delete=models.PROTECT, verbose_name='Категория')

    application_date = models.DateField(verbose_name='Дата Подачи', default=timezone.now)

    student_first_name = models.CharField(verbose_name='Имя', max_length=50)
    student_last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    student_middle_name = models.CharField(verbose_name='Отчество', max_length=50, blank=True)

    class Meta:
        verbose_name = "Заявление"
        verbose_name_plural = "Заявления"

    ############################
    # Template meta settings ###
    ############################
    update_header = 'Изменить данные заявления'
    create_header = 'Добавить заявление'
    list_header = 'Список заявлений'

    success_message_create = 'Заявление успешно создано'
    success_message_delete = 'Заявление успешно удалено'

    delete_modal_title = 'Удалить заявление'

    @property
    def update_url(self):
        return reverse('crud:statement-update', kwargs={'id': self.id})

    @property
    def delete_url(self):
        return reverse('crud:statement-delete', kwargs={'id': self.id})

    @property
    def create_url(self):
        return reverse('crud:statement-create')

    def __str__(self):
        return f'{self.student_first_name} {self.student_last_name} от {self.application_date.strftime("%d.%m.%Y")}'
