# Generated by Django 4.1.1 on 2023-08-08 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_remove_task_name_task_criteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='criteria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Blog.task'),
        ),
    ]