# Generated by Django 2.0.3 on 2018-03-23 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geoposts', '0015_auto_20180322_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geopost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('latitude', models.FloatField(blank=True, default=None, null=True)),
                ('longitude', models.FloatField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('city', models.CharField(blank=True, max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('experiment', models.ManyToManyField(to='geoposts.Experiment')),
                ('geoproject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geoposts.Geoproject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeopostStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('latitude', models.FloatField(blank=True, default=None, null=True)),
                ('longitude', models.FloatField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('city', models.CharField(blank=True, max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('result', jsonfield.fields.JSONField(default=dict)),
                ('done', models.BooleanField()),
                ('experiment', models.ManyToManyField(to='geoposts.Experiment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='geoposts',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='geoposts',
            name='geoproject',
        ),
        migrations.RemoveField(
            model_name='geoposts',
            name='image',
        ),
        migrations.RemoveField(
            model_name='geoposts',
            name='user',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.DeleteModel(
            name='Geoposts',
        ),
        migrations.AddField(
            model_name='geopoststudent',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geoposts.Image'),
        ),
        migrations.AddField(
            model_name='geopoststudent',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='geopost',
            name='image',
            field=models.ManyToManyField(to='geoposts.Image'),
        ),
    ]
