# Generated by Django 4.0.4 on 2022-06-23 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0003_answer_image_1_answer_image_2_answer_image_3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='parents_email',
        ),
        migrations.RemoveField(
            model_name='child',
            name='visit_time',
        ),
        migrations.RemoveField(
            model_name='child',
            name='visit_weekday',
        ),
    ]
