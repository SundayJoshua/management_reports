# Generated by Django 4.1.1 on 2023-09-01 06:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0028_calendar_alter_post_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='products_ordered',
        ),
        migrations.AlterField(
            model_name='calendar',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Calendar'),
        ),
    ]