# Generated by Django 5.1 on 2024-12-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_alter_brandmodel_established'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]