# Generated by Django 3.2 on 2021-04-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210413_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
