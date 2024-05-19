# Generated by Django 5.0.6 on 2024-05-08 22:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_consultation_reservation_type_reservation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='capacity_of_members',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='reservation',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
