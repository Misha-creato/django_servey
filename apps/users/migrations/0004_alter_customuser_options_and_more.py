# Generated by Django 4.2 on 2024-04-18 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_managers_customuser_token_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
