# Generated by Django 4.1.7 on 2023-05-07 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0003_treasurehunt_start_time_treasurehunt_time_taken_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treasurehunt',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='treasurehunt',
            name='time_taken',
        ),
    ]
