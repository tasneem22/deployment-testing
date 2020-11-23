# Generated by Django 3.1.3 on 2020-11-20 18:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thematic_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thematicpage',
            name='moderators',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='can_moderate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thematicpage',
            name='requested_by',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='requested_pages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thematicpage',
            name='users',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='can_view', to=settings.AUTH_USER_MODEL),
        ),
    ]