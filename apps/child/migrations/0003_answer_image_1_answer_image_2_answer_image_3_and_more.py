# Generated by Django 4.0.4 on 2022-06-04 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('child', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='answer_images'),
        ),
        migrations.AddField(
            model_name='answer',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='answer_images'),
        ),
        migrations.AddField(
            model_name='answer',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='answer_images'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer_employee', to=settings.AUTH_USER_MODEL),
        ),
    ]
