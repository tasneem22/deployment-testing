# Generated by Django 3.1.3 on 2020-11-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_upload_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]