# Generated by Django 4.1.7 on 2023-03-25 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogger_about_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogger',
            old_name='about_author',
            new_name='about_blogger',
        ),
    ]