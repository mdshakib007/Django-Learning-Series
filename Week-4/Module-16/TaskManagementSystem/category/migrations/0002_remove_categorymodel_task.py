# Generated by Django 5.1 on 2024-11-23 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='task',
        ),
    ]
