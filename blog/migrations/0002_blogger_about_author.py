# Generated by Django 4.1.7 on 2023-03-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='about_author',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
