# Generated by Django 4.0.1 on 2022-12-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0011_grades_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='quarter',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='quarter'),
        ),
    ]
