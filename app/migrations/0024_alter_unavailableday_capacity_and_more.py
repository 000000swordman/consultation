# Generated by Django 5.0.6 on 2024-05-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_unavailableday_consultation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unavailableday',
            name='capacity',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='unavailableday',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]