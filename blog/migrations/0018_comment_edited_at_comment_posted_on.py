# Generated by Django 4.1.7 on 2023-04-06 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_remove_comment_by_user_comment_commentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='posted_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
