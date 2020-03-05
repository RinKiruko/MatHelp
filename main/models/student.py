from django.db import models
from django.urls import reverse, reverse_lazy
from main.models.mixins import TemplateModelMetaInfoMixin

GENDER_CHOICES = (
    ('Male', 'Мужской'),
    ('Female', 'Женский'),
)


class Student(TemplateModelMetaInfoMixin, models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50, blank=True)
    gender = models.CharField(verbose_name='Пол', choices=GENDER_CHOICES, max_length=50)
    student_card_id = models.CharField(verbose_name='Номер студенческого билета', max_length=50)
    group = models.ForeignKey('main.Group', related_name='students', verbose_name='Группа', on_delete=models.CASCADE,
                              null=True)

    sorting_weight = models.FloatField(default=1.0)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('first_name', 'last_name')
        unique_together = ('student_card_id',)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.group.name})"

    # Template meta settings ###

    update_header = 'Изменить данные о студенте'
    create_header = 'Добавить студента'
    list_header = 'Список студентов'

    success_message_create = 'Студент успешно создан'
    success_message_delete = 'Студент успешно удален'

    delete_modal_title = 'Удалить студента'

    @property
    def update_url(self):
        return reverse('main:student-update', kwargs={'id': self.id})

    @property
    def delete_url(self):
        return reverse('main:student-delete', kwargs={'id': self.id})

    @property
    def create_url(self):
        return reverse('main:student-create')

    ############################
