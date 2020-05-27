from django.db import models


class Payment(models.Model):
    student_initial = models.CharField('Инициалы студента', blank=True, max_length=100)
    amount = models.DecimalField('Сумма выплаты', max_digits=7, decimal_places=2)
    date = models.DateField('Дата выплаты')
    statement = models.OneToOneField('crud.statement', related_name='payment', verbose_name='Заявление', null=True,
                                     on_delete=models.PROTECT)
    
    statement_category = models.ForeignKey('crud.StatementCategory', related_name='payments',
                                           verbose_name='Категория выплаты', null=True,
                                           on_delete=models.PROTECT, max_length=50)

    class Meta:
        verbose_name = "Выплата"
        verbose_name_plural = "Выплаты"

    def __str__(self):
        return f"{self.amount}р. от {self.date}"
