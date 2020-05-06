from main.forms import *
from main.fitlersets import StatementCategoryFilter, StatementFilter
from main.models import StatementCategory, Statement
from main.views.factories import list_view_factory, update_view_factory, create_view_factory, \
    create_add_another_view_factory, delete_view_factory

__all__ = (
    'StatementCategoryListView',
    'StatementCategoryUpdateView',
    'StatementCategoryCreateView',
    'StatementCategoryCreateAddAnotherView',
    'StatementCategoryDeleteView',

    'StatementListView',
    'StatementUpdateView',
    'StatementCreateView',
    'StatementCreateAddAnotherView',
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
                                                  'CRUD/update/index_layout.html')
StatementCategoryCreateView = create_view_factory(StatementCategory, StatementCategoryForm,
                                                  'CRUD/create/index_layout.html')
StatementCategoryCreateAddAnotherView = create_add_another_view_factory(StatementCategory, StatementCategoryForm,
                                                                        'CRUD/create/index_layout.html')
StatementCategoryDeleteView = delete_view_factory(StatementCategory)

################################################
# CRUD for statement model #####################
################################################
_statement_optimized_queryset = Statement.objects.prefetch_related(
    'student', 'statement_category', 'student__group',
)
_statement_filters_data = {}
StatementListView = list_view_factory(Statement, _statement_optimized_queryset,
                                      StatementFilter, _statement_filters_data,
                                      'CRUD/list/statement.html')
StatementUpdateView = update_view_factory(Statement, StatementForm,
                                          'CRUD/update/index_layout.html')
StatementCreateView = create_view_factory(Statement, StatementForm,
                                          'CRUD/create/index_layout.html')
StatementCreateAddAnotherView = create_add_another_view_factory(Statement, StatementForm,
                                                                'CRUD/create/index_layout.html')
StatementDeleteView = delete_view_factory(Statement)