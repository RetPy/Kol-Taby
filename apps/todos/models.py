from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    STATUS_CHOICE = (
        ('1', 'В процессе'),
        ('2', 'В ожидании'),
        ('4', 'Выполнено'),
    )
    title = models.CharField(
        max_length=255
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    deadline = models.DateTimeField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE
    )
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='task_employee',
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-id']

    def __str__(self):
        return str(self.title)
