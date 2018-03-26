from django.db import models
from django.conf import settings
from PIL import Image
import jsonfield


class Geoproject(models.Model):
    name = models.CharField(max_length=250, blank=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return str(self.name)

    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Experiment(models.Model):
    experiment_name = models.CharField(max_length =250,blank =True)
    result = models.CharField(max_length = 250,blank = True)

    def __str__(self):
        return self.experiment_name



class Image(models.Model):
    name = models.CharField(max_length = 20,blank=True)
    image = models.ImageField()


    def __str__(self):
        return self.name + "_image"

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













