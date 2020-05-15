from crud.forms.base import BaseModelForm
from crud.models import Statement


class StatementForm(BaseModelForm):
    class Meta:
        model = Statement
        exclude = ('',)
