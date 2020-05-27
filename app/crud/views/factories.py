from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Model
from django.db.models import QuerySet
from django.forms import Form
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView
from django.views.generic.edit import BaseDeleteView
from django_filters import FilterSet
from django_filters.views import FilterView

from crud.views.mixins import *

__all__ = [
    'list_view_factory',
    'update_view_factory',
    'create_view_factory',
    # 'create_add_another_view_factory',
    'delete_view_factory',
]


def list_view_factory(model_class: type(Model), initial_queryset: QuerySet = None,
                      filterset_class: type(FilterSet) = None, filters_data: dict = None,
                      template_name=None):
    filtered_model_list_view = type(
        f'Filtered{model_class.__name__}ListView',
        (FilterView,),
        {
            'model': model_class,
            'template_name': template_name,
            'filterset_class': filterset_class,
            'queryset': initial_queryset.order_by('-id'),
            'extra_context': {
                'list_header': model_class.list_header,
                'create_url': reverse_lazy(f'crud:{model_class.__name__.lower()}-create'),
                'delete_modal_title': model_class.delete_modal_title,

                'filters_data': filters_data,
            }
        }
    )

    return filtered_model_list_view


def update_view_factory(model_class: type(Model), form_class: type(Form), template_name=None):
    update_model_view = type(
        f'Update{model_class.__name__}View',
        (SuccessMessageMixin, UpdateView,),
        {
            'model': model_class,
            'success_message': model_class.success_message_update,
            'template_name': template_name,
            'form_class': form_class,
            'pk_url_kwarg': 'id',
            'success_url': reverse_lazy(f'crud:{model_class.__name__.lower()}-list'),
            'extra_context': {
                'update_header': model_class.update_header,
            },
        }

    )
    return update_model_view


def create_view_factory(model_class: type(Model), form_class: type(Form), template_name=None):
    create_model_view = type(
        f'Create{model_class.__name__}View',
        (SuccessMessageMixin, CreateView,),
        {
            'model': model_class,
            'template_name': template_name,
            'form_class': form_class,
            'get_success_url': lambda self: reverse(f'crud:{model_class.__name__.lower()}-update',
                                                    kwargs={'id': self.object.id}),
            'success_message': model_class.success_message_create,
            'extra_context': {
                'create_header': model_class.create_header,
                'create_url': reverse_lazy(f'crud:{model_class.__name__.lower()}-create'),
                'create_add_another_url': reverse_lazy(f'crud:{model_class.__name__.lower()}-create-add-another'),
            },
        }
    )
    return create_model_view


def create_add_another_view_factory(model_class: type(Model), form_class: type(Form), template_name=None):
    create_add_another_view = create_view_factory(model_class, form_class, template_name)
    create_add_another_view.success_url = reverse_lazy(
        f'crud:{model_class.__name__.lower()}-create-add-another'
    ),
    return create_add_another_view


def delete_view_factory(model_class: type(Model)):
    delete_model_view = type(
        f'Delete{model_class.__name__}View',
        (SuccessMessageDeleteMixin, BaseDeleteView,),
        {
            'model': model_class,
            'success_message': model_class.success_message_delete,
            'pk_url_kwarg': 'id',
            'success_url': reverse_lazy(f'crud:{model_class.__name__.lower()}-list'),
        }
    )
    return delete_model_view
