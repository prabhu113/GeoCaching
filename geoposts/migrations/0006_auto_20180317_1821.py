# Generated by Django 2.0.2 on 2018-03-18 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geoposts', '0005_auto_20180317_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoposts',
            name='geoproject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geoposts.Geoproject'),
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
    ]
