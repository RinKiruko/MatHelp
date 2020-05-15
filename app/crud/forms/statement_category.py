from crud.forms.base import BaseModelForm
from crud.models import StatementCategory


class StatementCategoryForm(BaseModelForm):
    class Meta:
        model = StatementCategory
        exclude = ('',)
