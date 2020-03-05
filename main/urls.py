from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import *

app_name = "main"
urlpatterns = [
    # Students
    path('students/list/', StudentListView.as_view(), name='student-list'),
    path('students/create/', StudentCreateView.as_view(), name='student-create'),
    path('students/create-add-another/', StudentCreateAddAnotherView.as_view(), name='student-create-add-another'),
    path('students/update/<int:id>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/delete/<int:id>/', StudentDeleteView.as_view(), name='student-delete'),

    # Groups
    path('groups/list/', GroupListView.as_view(), name='group-list'),
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/create-add-another/', GroupCreateAddAnotherView.as_view(), name='group-create-add-another'),
    path('groups/update/<int:id>/', GroupUpdateView.as_view(), name='group-update'),
    path('groups/delete/<int:id>/', GroupDeleteView.as_view(), name='group-delete'),

    # Categories
    path('statementcategories/list/', StatementCategoryListView.as_view(), name='statementcategory-list'),
    path('statementcategories/create/', StatementCategoryCreateView.as_view(), name='statementcategory-create'),
    path('statementcategories/create-add-another/', StatementCategoryCreateAddAnotherView.as_view(),
         name='statementcategory-create-add-another'),
    path('statementcategories/update/<int:id>/', StatementCategoryUpdateView.as_view(),
         name='statementcategory-update'),
    path('statementcategories/delete/<int:id>/', StatementCategoryDeleteView.as_view(),
         name='statementcategory-delete'),

    # Statements
    path('statements/list/', StatementListView.as_view(), name='statement-list'),
    path('statements/create/', StatementCreateView.as_view(), name='statement-create'),
    path('statements/create-add-another/', StatementCreateAddAnotherView.as_view(),
         name='statement-create-add-another'),
    path('statements/update/<int:id>/', StatementUpdateView.as_view(),
         name='statement-update'),
    path('statements/delete/<int:id>/', StatementDeleteView.as_view(),
         name='statement-delete'),

    # path('distribute/',)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
