# Generated by Django 3.1.3 on 2020-11-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20201117_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='link',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
