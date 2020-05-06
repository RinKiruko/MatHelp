from main.forms.base import BaseModelForm
from main.models import Statement


class StatementForm(BaseModelForm):
    class Meta:
        model = Statement
        exclude = ('',)
