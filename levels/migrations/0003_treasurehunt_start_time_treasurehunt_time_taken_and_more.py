# Generated by Django 4.1.7 on 2023-05-07 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0002_alter_treasurehunt_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasurehunt',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treasurehunt',
            name='time_taken',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='treasurehunt',
            name='level',
            field=models.IntegerField(choices=[(1, 'level1'), (2, 'level2'), (3, 'level3'), (4, 'level4'), (5, 'level5'), (6, 'level6'), (7, 'level7'), (8, 'level8')]),
        ),
    ]
