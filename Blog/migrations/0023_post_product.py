# Generated by Django 4.1.1 on 2023-08-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0022_remove_post_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='product',
            field=models.ManyToManyField(to='Blog.product'),
        ),
    ]