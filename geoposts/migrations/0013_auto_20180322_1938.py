# Generated by Django 2.0.3 on 2018-03-23 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoposts', '0012_auto_20180322_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoposts',
            name='geoproject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geoposts.Geoproject'),
        ),
    ]