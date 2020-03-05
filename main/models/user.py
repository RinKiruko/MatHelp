from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True, )
    username = models.CharField(
        max_length=150,
        blank=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password', 'username')
