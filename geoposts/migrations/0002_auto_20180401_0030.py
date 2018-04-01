# Generated by Django 2.0.3 on 2018-04-01 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geoposts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_name', models.CharField(blank=True, max_length=250)),
                ('result', models.CharField(blank=True, max_length=250)),
            ],
        ),
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
            ],
            options={
                'verbose_name': 'Specimen-List',
                'verbose_name_plural': 'Specimen-List',
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
                ('result', jsonfield.fields.JSONField()),
                ('done', models.BooleanField()),
                ('geo_post_id', models.CharField(blank=True, max_length=250)),
                ('experiment', models.ManyToManyField(to='geoposts.Experiment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(blank=True, max_length=250)),
                ('image', models.ImageField(upload_to='geocaching_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='geoposts',
            name='geoproject',
        ),
        migrations.AlterModelOptions(
            name='geoproject',
            options={'verbose_name': 'Geo-Caching Project', 'verbose_name_plural': 'Geo-Caching Projects'},
        ),
        migrations.RemoveField(
            model_name='geoproject',
            name='user',
        ),
        migrations.AddField(
            model_name='geoproject',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
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
            name='geoproject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geoposts.Geoproject'),
        ),
        migrations.AddField(
            model_name='geopost',
            name='image',
            field=models.ManyToManyField(to='geoposts.Image'),
        ),
    ]
