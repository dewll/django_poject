# Generated by Django 4.0.2 on 2022-03-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default='2022-03-27-08:05:55'),
        ),
    ]
