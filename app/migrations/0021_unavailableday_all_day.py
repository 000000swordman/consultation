# Generated by Django 5.0.6 on 2024-05-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_unavailableday'),
    ]

    operations = [
        migrations.AddField(
            model_name='unavailableday',
            name='all_day',
            field=models.BooleanField(default=False),
        ),
    ]
