# Generated by Django 4.1.1 on 2023-08-23 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0019_alter_post_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
    ]
