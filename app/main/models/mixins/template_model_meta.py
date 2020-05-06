from abc import ABC, abstractmethod


class TemplateModelMetaInfoMixin:
    _list_header = None
    success_message_update = 'Изменения сохранены'

    @property
    @abstractmethod
    def success_message_create(self):
        ...

    @property
    @abstractmethod
    def success_message_delete(self):
        ...

    @property
    @abstractmethod
    def delete_modal_title(self):
        ...

    @property
    @abstractmethod
    def create_url(self):
        ...

    @property
    @abstractmethod
    def update_url(self):
        ...

    @property
    @abstractmethod
    def delete_url(self):
        ...

    @property
    @abstractmethod
    def list_header(self):
        ...

    @property
    @abstractmethod
    def create_header(self):
        ...

    @property
    @abstractmethod
    def update_header(self):
        ...
