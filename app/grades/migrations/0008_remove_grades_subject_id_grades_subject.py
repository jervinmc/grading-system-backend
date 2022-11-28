# Generated by Django 4.0.1 on 2022-11-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0007_remove_grades_date_from_grades_date_submitted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='subject_id',
        ),
        migrations.AddField(
            model_name='grades',
            name='subject',
            field=models.IntegerField(default=0, verbose_name='subject'),
        ),
    ]