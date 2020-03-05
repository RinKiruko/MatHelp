from django.db import models
from django.urls import reverse

from main.models.mixins import TemplateModelMetaInfoMixin


class Statement(TemplateModelMetaInfoMixin, models.Model):
    requested_payment = models.DecimalField(verbose_name='Запрашиваемая сумма', max_digits=7, decimal_places=2)
    payed_payment = models.DecimalField(verbose_name='Сумма выплаты', null=True, max_digits=7, decimal_places=2)
    application_date = models.DateField(verbose_name='Дата подачи')

    statement_category = models.ForeignKey('main.StatementCategory', related_name='statements', on_delete=models.PROTECT,
                                           verbose_name='Категория')
    student = models.ForeignKey('main.Student', related_name='statements', on_delete=models.PROTECT,
                                verbose_name='Кем подано')

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
        return reverse('main:statement-update', kwargs={'id': self.id})

    @property
    def delete_url(self):
        return reverse('main:statement-delete', kwargs={'id': self.id})

    @property
    def create_url(self):
        return reverse('main:statement-create')

    def __str__(self):
        return f'{self.student} от {self.application_date.strftime("%d.%m.%Y")}'
