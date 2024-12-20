# Generated by Django 5.1 on 2024-11-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('post', '0002_post_updated_at_alter_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='post_category', to='category.category'),
        ),
    ]
