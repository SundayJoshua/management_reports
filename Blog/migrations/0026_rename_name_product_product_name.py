# Generated by Django 4.1.1 on 2023-08-23 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0025_product_post_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]