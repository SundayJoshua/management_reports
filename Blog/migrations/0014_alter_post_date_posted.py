# Generated by Django 4.1.1 on 2023-08-18 09:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_post_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
