# Generated by Django 5.0.6 on 2024-05-16 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_reservation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='is_full',
        ),
    ]
