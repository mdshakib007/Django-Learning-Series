# Generated by Django 5.1 on 2024-12-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='price',
            field=models.IntegerField(),
        ),
    ]
