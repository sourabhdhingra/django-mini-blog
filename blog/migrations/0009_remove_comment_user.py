# Generated by Django 4.1.7 on 2023-03-27 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
