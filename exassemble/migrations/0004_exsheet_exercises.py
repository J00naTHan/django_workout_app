# Generated by Django 5.0 on 2023-12-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exassemble', '0003_rename_exercises_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='exsheet',
            name='exercises',
            field=models.ManyToManyField(to='exassemble.exercise'),
        ),
    ]
