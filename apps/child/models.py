from django.db import models

from apps.users.models import User


class Child(models.Model):
    GENDER_CHOICE = (
        ('1', 'Мужской'),
        ('2', 'Женский'),
        ('4', 'Другое'),
    )
    WEEKDAY_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
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
    parents_fio = models.CharField(
        max_length=500,
    )
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICE,
    )
    parents_phone_number = models.CharField(
        max_length=15,
    )
    parents_email = models.EmailField(
        unique=True,
    )
    address = models.CharField(
        max_length=100,
    )
    diagnosis = models.CharField(
        max_length=150,
    )
    visit_weekday = models.CharField(
        max_length=15,
        choices=WEEKDAY_CHOICE,
    )
    visit_time = models.TimeField()
    exercises = models.TextField()
    employee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='child_employee',
        null=True,
        blank=True,
    )
    questions = models.JSONField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Ребёнок'
        verbose_name_plural = 'Дети'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Answer(models.Model):
    date = models.DateField(
        auto_now_add=True,
    )
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='answer_employee',
    )
    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name='answer_child',
    )
    quiz = models.JSONField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.child}: {self.date}'
