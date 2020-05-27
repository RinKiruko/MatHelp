from crud.forms import *
from crud.fitlersets import StatementCategoryFilter, StatementFilter
from crud.models import StatementCategory, Statement
from crud.views.factories import *

__all__ = (
    'StatementCategoryListView',
    'StatementCategoryUpdateView',
    'StatementCategoryCreateView',
    # 'StatementCategoryCreateAddAnotherView',
    'StatementCategoryDeleteView',

    'StatementListView',
    'StatementUpdateView',
    'StatementCreateView',
    # 'StatementCreateAddAnotherView',
    'StatementDeleteView',
)


################################################
# CRUD for statement category model ############
################################################

_statementcategory_optimized_queryset = StatementCategory.objects.prefetch_related(
    'statements'
)

StatementCategoryListView = list_view_factory(StatementCategory, _statementcategory_optimized_queryset,
                                              StatementCategoryFilter, {},
                                              'CRUD/list/statementcategory.html')
StatementCategoryUpdateView = update_view_factory(StatementCategory, StatementCategoryForm,
                                                  'CRUD/update/base.html')
StatementCategoryCreateView = create_view_factory(StatementCategory, StatementCategoryForm,
                                                  'CRUD/create/base.html')
# StatementCategoryCreateAddAnotherView = create_add_another_view_factory(StatementCategory, StatementCategoryForm,
#                                                                         'CRUD/create/base.html')
StatementCategoryDeleteView = delete_view_factory(StatementCategory)

################################################
# CRUD for statement model #####################
################################################
_statement_optimized_queryset = Statement.objects.select_related('statement_category',)
_statement_filters_data = {}

StatementListView = list_view_factory(Statement, _statement_optimized_queryset,
                                      StatementFilter, _statement_filters_data,
                                      'CRUD/list/statement.html')
StatementUpdateView = update_view_factory(Statement, StatementForm,
                                          'CRUD/update/base.html')
StatementCreateView = create_view_factory(Statement, StatementForm,
                                          'CRUD/create/base.html')
# StatementCreateAddAnotherView = create_add_another_view_factory(Statement, StatementForm,
#                                                                 'CRUD/create/base.html')
StatementDeleteView = delete_view_factory(Statement)
