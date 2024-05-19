# Generated by Django 5.0.6 on 2024-05-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_member_reservation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='capacity_of_members',
        ),
        migrations.AddField(
            model_name='consultation',
            name='capacity_of_members',
            field=models.IntegerField(default=10),
        ),
        migrations.DeleteModel(
            name='Member_Reservation',
        ),
    ]
