# Generated by Django 4.1.1 on 2023-08-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0026_rename_name_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contact',
            field=models.CharField(max_length=128, null=True),
        ),
    ]