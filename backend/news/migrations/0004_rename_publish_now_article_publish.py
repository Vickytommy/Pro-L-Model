# Generated by Django 3.2 on 2021-04-13 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='publish_now',
            new_name='publish',
        ),
    ]
