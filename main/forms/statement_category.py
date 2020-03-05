from main.forms.base import BaseModelForm
from main.models import StatementCategory


class StatementCategoryForm(BaseModelForm):
    class Meta:
        model = StatementCategory
        exclude = ('',)
