from general.forms.base import BaseBoostrapForm
from crud.models import StatementCategory


class StatementCategoryForm(BaseBoostrapForm):
    class Meta:
        model = StatementCategory
        exclude = ('',)
