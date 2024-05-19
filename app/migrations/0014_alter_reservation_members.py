# Generated by Django 5.0.6 on 2024-05-09 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_reservation_type_consultation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
