# Generated by Django 2.0.3 on 2018-04-16 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoposts', '0010_auto_20180416_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor_results',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='geoposts.Geoproject'),
            preserve_default=False,
        ),
    ]