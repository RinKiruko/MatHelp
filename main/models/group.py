from django.db import models
from django.urls import reverse

from main.models.mixins import TemplateModelMetaInfoMixin

STUDYING_TYPE_CHOICES = (
    ('under', 'Бакалавриат'),
    ('graduated', 'Магистратура'),
    ('specialist', 'Специалитет'),
    ('post', 'Аспирантура'),
)


class Group(TemplateModelMetaInfoMixin, models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, unique=True)

    studying_level = models.CharField(verbose_name='Ступень обучения', choices=STUDYING_TYPE_CHOICES, max_length=50)
    course = models.IntegerField(verbose_name='Курс', )

    chief = models.ForeignKey('main.Student', related_name='chief', null=True, blank=True, verbose_name='Староста',
                              on_delete=models.SET_NULL)

    # Template meta settings ###
    update_header = 'Изменить данные о группе'
    create_header = 'Добавить группу'
    list_header = 'Список групп'

    success_message_create = 'Группа успешно создана'
    success_message_delete = 'Группа успешно удалена'

    delete_modal_title = 'Удалить группу'

    @property
    def update_url(self):
        return reverse('main:group-update', kwargs={'id': self.id})

    @property
    def delete_url(self):
        return reverse('main:group-delete', kwargs={'id': self.id})

    @property
    def create_url(self):
        return reverse('main:group-create')

    ############################

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f'{self.name}'

    def get_studying_type(self):
        for choice in STUDYING_TYPE_CHOICES:
            if choice[0] == self.studying_level:
                return choice[1]

        return 'Не указано'
