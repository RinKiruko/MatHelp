from django.urls import path

from crud.views import *

app_name = "crud"
urlpatterns = [
    # Categories
    path('statementcategories/list/', StatementCategoryListView.as_view(), name='statementcategory-list'),
    path('statementcategories/create/', StatementCategoryCreateView.as_view(), name='statementcategory-create'),
    # path('statementcategories/create-add-another/', StatementCategoryCreateAddAnotherView.as_view(),
    #      name='statementcategory-create-add-another'),
    path('statementcategories/update/<int:id>/', StatementCategoryUpdateView.as_view(),
         name='statementcategory-update'),
    path('statementcategories/delete/<int:id>/', StatementCategoryDeleteView.as_view(),
         name='statementcategory-delete'),

    # Statements
    path('statements/list/', StatementListView.as_view(), name='statement-list'),
    path('statements/create/', StatementCreateView.as_view(), name='statement-create'),
    # path('statements/create-add-another/', StatementCreateAddAnotherView.as_view(),
    #      name='statement-create-add-another'),
    path('statements/update/<int:id>/', StatementUpdateView.as_view(),
         name='statement-update'),
    path('statements/delete/<int:id>/', StatementDeleteView.as_view(),
         name='statement-delete'),
]
