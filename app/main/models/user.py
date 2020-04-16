from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password', 'username')

    objects = UserManager()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
