# Generated by Django 4.1.1 on 2023-08-23 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0016_remove_post_products_post_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='evidence',
        ),
    ]
