# Generated by Django 3.1.3 on 2020-11-22 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thematic_pages', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.IntegerField(choices=[(0, 'Document'), (1, 'Image'), (2, 'Video'), (3, 'Link')], default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(0, 'Rejected'), (1, 'Approved'), (2, 'Pending')], default=2)),
                ('innopoints', models.IntegerField(default=0)),
                ('link', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('rating', models.FloatField(blank=True, default=0, null=True)),
                ('file', models.FileField(blank=True, default='files/None/No-doc.pdf', null=True, upload_to='files/')),
                ('tags', models.ManyToManyField(blank=True, default=None, null=True, to='storage.Tag')),
                ('thematic_page', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='thematic_pages.thematicpage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='storage.upload')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='BookmarkPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploads', models.ManyToManyField(null=True, to='storage.Upload')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
