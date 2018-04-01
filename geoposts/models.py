from django.db import models
from django.conf import settings
from PIL import Image as im
import jsonfield
from django.contrib.auth.models import AbstractBaseUser


class Meta:
    app_label = 'Project-Data'


class Geoproject(models.Model):
    name = models.CharField(max_length=250, blank=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)



    class Meta:
        verbose_name = 'Geo-Caching Project'

        verbose_name_plural = 'Geo-Caching Projects'

    def __str__(self):
        return str(self.name)

    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Experiment(models.Model):
    experiment_name = models.CharField(max_length =250,blank =True)
    result = models.CharField(max_length = 250,blank = True)

    def __str__(self):
        return self.experiment_name



class Image(models.Model):
    image_name = models.CharField(max_length=250,blank=True)
    image = models.ImageField(upload_to='geocaching_images')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            given_name = self.image.name
            self.image_name = given_name
        except:
            pass


        super(Image, self).save()

        return self.id

    def __str__(self):
        return self.image_name

class CommonGeo(models.Model):
    name = models.CharField(max_length=250, blank=True)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    city = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        abstract = True

class Geopost(CommonGeo):
    image = models.ManyToManyField(Image)
    geoproject = models.ForeignKey(Geoproject, on_delete=models.CASCADE)
    experiment = models.ManyToManyField(Experiment)

    class Meta:
        verbose_name = 'Specimen-List'

        verbose_name_plural = 'Specimen-List'

    def __str__(self):
        return (self.name)

class GeopostStudent(CommonGeo):
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null = True)
    experiment = models.ManyToManyField(Experiment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    result = jsonfield.JSONField()
    done = models.BooleanField(blank = True)
    geo_post_id = models.CharField(max_length = 250,blank= True)

    def get_absolute_url(self):
        return "/students/{0}".format(self.user.id)














