# Generated by Django 3.0.1 on 2020-03-04 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200304_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='credientials',
            new_name='credentials',
        ),
    ]
