# Generated by Django 4.1.1 on 2023-08-23 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0023_post_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
