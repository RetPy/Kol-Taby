# Generated by Django 4.0.4 on 2022-05-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('quiz', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('patronymic', models.CharField(blank=True, max_length=150, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('parents_fio', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('1', 'Мужской'), ('2', 'Женский'), ('4', 'Другое')], max_length=50)),
                ('parents_phone_number', models.CharField(max_length=15)),
                ('parents_email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('diagnosis', models.CharField(max_length=150)),
                ('visit_date_time', models.DateTimeField()),
                ('exercises', models.TextField()),
                ('questions', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Ребёнок',
                'verbose_name_plural': 'Дети',
            },
        ),
    ]