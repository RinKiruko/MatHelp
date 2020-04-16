from app.main.forms.base import BaseModelForm
from app.main.models import StatementCategory


class StatementCategoryForm(BaseModelForm):
    class Meta:
        model = StatementCategory
        exclude = ('',)
