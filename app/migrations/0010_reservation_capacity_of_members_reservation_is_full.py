# Generated by Django 5.0.6 on 2024-05-08 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_reservation_consultation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='capacity_of_members',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='reservation',
            name='is_full',
            field=models.BooleanField(default=False),
        ),
    ]
