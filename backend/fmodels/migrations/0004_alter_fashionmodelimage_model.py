# Generated by Django 3.2 on 2021-05-02 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmodels', '0003_rename_images_fashionmodelimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashionmodelimage',
            name='model',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fmodels.fashionmodel'),
        ),
    ]