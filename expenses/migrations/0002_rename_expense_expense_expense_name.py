# Generated by Django 4.1.1 on 2023-09-01 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='expense',
            new_name='expense_name',
        ),
    ]
