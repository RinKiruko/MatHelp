from main.fitlersets import *
from main.forms import *
from main.models import *
from main.models.group import STUDYING_TYPE_CHOICES
from main.views.factories import *

__all__ = (
    'StudentListView',
    'StudentUpdateView',
    'StudentCreateView',
    'StudentCreateAddAnotherView',
    'StudentDeleteView',

    'GroupListView',
    'GroupUpdateView',
    'GroupCreateView',
    'GroupCreateAddAnotherView',
    'GroupDeleteView',

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
# CRUD for student model #######################
################################################
_student_filters_data = {
    'study_levels': STUDYING_TYPE_CHOICES,
}
_student_optimized_queryset = Student.objects.select_related(
    'group',
).prefetch_related(
    'statements',
)

StudentListView = list_view_factory(Student, _student_optimized_queryset, StudentFilter,
                                    _student_filters_data, 'CRUD/list/student.html')

StudentUpdateView = update_view_factory(Student, StudentForm, 'CRUD/update/base.html')

StudentCreateView = create_view_factory(Student, StudentForm, 'CRUD/create/base.html')
StudentCreateAddAnotherView = create_add_another_view_factory(Student, StudentForm, 'CRUD/create/base.html')

StudentDeleteView = delete_view_factory(Student)

################################################
# CRUD for group model #########################
################################################
_group_optimized_queryset = Group.objects.prefetch_related(
    'students'
).select_related(
    'chief'
)
_group_filters_data = {
    'study_levels': STUDYING_TYPE_CHOICES,
}
GroupListView = list_view_factory(Group, _group_optimized_queryset, GroupFilter, _group_filters_data,
                                  'CRUD/list/group.html')
GroupUpdateView = update_view_factory(Group, GroupForm, 'CRUD/update/base.html')
GroupCreateView = create_view_factory(Group, GroupForm, 'CRUD/create/base.html')
GroupCreateAddAnotherView = create_add_another_view_factory(Group, GroupForm, 'CRUD/create/base.html')
GroupDeleteView = delete_view_factory(Group)

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
StatementCategoryCreateAddAnotherView = create_add_another_view_factory(StatementCategory, StatementCategoryForm,
                                                                        'CRUD/create/base.html')
StatementCategoryDeleteView = delete_view_factory(StatementCategory)

################################################
# CRUD for statement model #####################
################################################
_statement_optimized_queryset = Statement.objects.prefetch_related(
    'student', 'statement_category', 'student__group',
)
_statement_filters_data = {
    'study_levels': STUDYING_TYPE_CHOICES,
}
StatementListView = list_view_factory(Statement, _statement_optimized_queryset,
                                      StatementFilter, _statement_filters_data,
                                      'CRUD/list/statement.html')
StatementUpdateView = update_view_factory(Statement, StatementForm,
                                          'CRUD/update/base.html')
StatementCreateView = create_view_factory(Statement, StatementForm,
                                          'CRUD/create/base.html')
StatementCreateAddAnotherView = create_add_another_view_factory(Statement, StatementForm,
                                                                'CRUD/create/base.html')
StatementDeleteView = delete_view_factory(Statement)
