# Generated by Django 2.1.8 on 2019-05-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190509_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredient',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='tag',
            new_name='tags',
        ),
    ]
