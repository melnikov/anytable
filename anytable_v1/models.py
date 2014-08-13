# coding=utf-8
from django.db import models
from south.modelsinspector import add_introspection_rules
from imagekit.models import ImageSpecField
from imagekit.processors import *
from image_cropping import ImageCropField, ImageRatioField

from django.contrib.auth.models import AbstractBaseUser




add_introspection_rules([], ["^sorl\.thumbnail\.fields\.ImageWithThumbnailField"])

# Create your models here.

class testUsers(models.Model):
    firstName = models.CharField(max_length=255,verbose_name="Имя")
    lastName = models.CharField(max_length=255,verbose_name="Фамилия")
    def __unicode__(self):
        return "gaga"

class testCities(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField(default=0)

class subscriber(models.Model):
    name = models.CharField(max_length=255, default="")
    logIn = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    def __unicode__(self):
        return u"%s" % self.name

class venueType(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name
class venueKitchen(models.Model):
    name = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return u"%s" % self.name

class region(models.Model):
    name = models.CharField(max_length=255, verbose_name="Region Name",default="")
    def __unicode__(self):
        return u"%s" % self.name

class city(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(region)
    def __unicode__(self):
        return u"%s" % self.name


class venue(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    address = models.CharField(max_length=255, verbose_name="Address")

    image = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})
    cropping = ImageRatioField('image', '430x360', free_crop=True)

    subscriber = models.ForeignKey(subscriber,null=True)
    #type = models.ForeignKey(venueType, null=True)
    type = models.ManyToManyField(venueType, null=False)
    city = models.ForeignKey(city, null=True)
    #photo = models.ManyToManyField(to=photo, null=True, blank=True)
    tel = models.CharField(max_length=255, blank=True, verbose_name="Telephone")
    email = models.CharField(max_length=255, blank=True, verbose_name="E-Mail")
    website = models.CharField(max_length=255, blank=True, verbose_name="Website")
    schedule = models.CharField(max_length=255, blank=True, verbose_name="Work Schedule")
    description = models.TextField(blank=True, verbose_name="Description")
    kitchen = models.ManyToManyField(venueKitchen,blank=True, verbose_name="Kitchen")

    def types_list(self):
        return ([v.name for v in self.type.all()])
    def kitchen_list(self):
        return ([k.name for k in self.kitchen.all()])

    def vkfield(self):
        return u"<h3>%s</h3>" % self.name

    vkfield.allow_tags = True

    def __unicode__(self):
       return u"%s " % self.name

class venueimage(models.Model):

    image = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(300, 150)], format='JPEG', options={'quality': 60})
    description = models.CharField(max_length=255)
    venue = models.ForeignKey(venue, null=True)

class event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', blank=True,null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(325, 186)], format='JPEG', options={'quality': 60})
    date = models.DateTimeField()
    #photo = models.ManyToManyField(to=photo, blank=True)
    QR = models.CharField(max_length=1024, default='')
    venue = models.ForeignKey(venue)

class user(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField('email address', unique=True, db_index=True)
    #password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey(city)
    joined = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email
