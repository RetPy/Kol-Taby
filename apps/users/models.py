from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import MyUserManager


class User(AbstractUser):
    username = None
    alias = models.CharField(
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )
    patronymic = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=255,
    )
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'alias'

    objects = MyUserManager()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.alias}'
