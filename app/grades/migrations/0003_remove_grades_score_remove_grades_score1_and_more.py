# Generated by Django 4.0.1 on 2022-11-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_grades_score1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='score1',
        ),
        migrations.AddField(
            model_name='grades',
            name='scores',
            field=models.IntegerField(default=0, verbose_name='scores'),
        ),
    ]
