from django.db import models
from django.urls import reverse

from crud.models.mixins import TemplateModelMetaInfoMixin


class StatementCategory(TemplateModelMetaInfoMixin, models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=50)
    legal_number = models.CharField(verbose_name='Юридический номер', max_length=50, unique=True)
    maximum_payment = models.DecimalField(verbose_name='Максимальная выплата', max_digits=7, decimal_places=2,
                                          blank=True, null=True)
    # TODO Replace with periodic payment
    necessarily_paying = models.BooleanField(verbose_name='Обязательна к выплате', default=False)
    
    weight = models.FloatField(verbose_name='Приоритет', default=1.0)

    # Template meta settings ###
    update_header = 'Изменить данные о категории'
    create_header = 'Добавить категорию выплат'
    list_header = 'Список категорий'

    success_message_create = 'Категория успешно создана'
    success_message_delete = 'Категория успешно удалена'

    delete_modal_title = 'Удалить категорию'

    @property
    def update_url(self):
        return reverse('crud:statementcategory-update', kwargs={'id': self.id})

    @property
    def delete_url(self):
        return reverse('crud:statementcategory-delete', kwargs={'id': self.id})

    @property
    def create_url(self):
        return reverse('crud:statementcategory-create')

    ############################

    class Meta:
        verbose_name = 'Категория заявления'
        verbose_name_plural = 'Категории заявлений'

    def __str__(self):
        return f'{self.title}'
