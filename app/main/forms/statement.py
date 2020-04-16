from app.main.forms.base import BaseModelForm
from app.main.models import Statement


class StatementForm(BaseModelForm):
    class Meta:
        model = Statement
        exclude = ('',)
