from general.forms.base import BaseBoostrapForm
from crud.models import Statement


class StatementForm(BaseBoostrapForm):
    class Meta:
        model = Statement
        exclude = ('',)
