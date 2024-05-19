# Generated by Django 5.0.6 on 2024-05-08 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_consultation_capacity_of_members_reservation_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='day_of_week',
            field=models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=9, verbose_name='day'),
        ),
    ]