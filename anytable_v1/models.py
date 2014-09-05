# coding=utf-8
from django.db import models
from south.modelsinspector import add_introspection_rules
from imagekit.models import ImageSpecField
from imagekit.processors import *
from image_cropping import ImageCropField, ImageRatioField
from pygeocoder import *
from django.contrib.auth.models import AbstractBaseUser




add_introspection_rules([], ["^sorl\.thumbnail\.fields\.ImageWithThumbnailField"])

# Create your models here.

class TestUsers(models.Model):
    firstName = models.CharField(max_length=255,verbose_name="Имя")
    lastName = models.CharField(max_length=255,verbose_name="Фамилия")
    def __unicode__(self):
        return "gaga"

class TestCities(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField(default=0)

class Subscriber(models.Model):
    name = models.CharField(max_length=255, default="")
    logIn = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    def __unicode__(self):
        return u"%s" % self.name

class VenueType(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name
class VenueKitchen(models.Model):
    name = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return u"%s" % self.name

class VenueOptions(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return u"%s" % self.name

class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name="Region Name",default="")
    def __unicode__(self):
        return u"%s" % self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return u"%s" % self.name


class Venue(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    image = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})
    cropping = ImageRatioField('image', '220x170', free_crop=False)
    option = models.ManyToManyField(VenueOptions, null=True)
    subscriber = models.ForeignKey(Subscriber,null=True)
    #type = models.ForeignKey(venueType, null=True)
    type = models.ManyToManyField(VenueType, null=False)
    city = models.ForeignKey(City, null=True)
    address = models.TextField(blank=True, verbose_name="Address")
    facebook_url = models.CharField(max_length=1024, verbose_name="Facebook URL", blank=True, null=True)
    vk_url = models.CharField(max_length=1024, verbose_name="VK URL", blank=True, null=True)
    #photo = models.ManyToManyField(to=photo, null=True, blank=True)
    tel = models.CharField(max_length=255, blank=True, verbose_name="Telephone")
    email = models.CharField(max_length=255, blank=True, verbose_name="E-Mail")
    website = models.CharField(max_length=255, blank=True, verbose_name="Website")
    schedule = models.CharField(max_length=255, blank=True, verbose_name="Work Schedule")
    description = models.TextField(blank=True, verbose_name="Description")
    kitchen = models.ManyToManyField(VenueKitchen,blank=True, verbose_name="Kitchen")

    def types_list(self):
        return ([v.name for v in self.type.all()])
    def kitchen_list(self):
        return ([k.name for k in self.kitchen.all()])
    def option_list(self):
        return ([o.name for o in self.option.all()])
    def vkfield(self):
        return u"<h3>%s</h3>" % self.name

    vkfield.allow_tags = True

    def __unicode__(self):
       return u"%s " % self.name

class Venueimage(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(300, 150)], format='JPEG', options={'quality': 60})
    description = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue, null=True)

class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', blank=True,null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(325, 186)], format='JPEG', options={'quality': 60})
    date = models.DateTimeField()
    event_date = models.DateField(null=True)
    event_time = models.TimeField(null=True)
    description = models.TextField(blank=True, verbose_name="Description")
    #photo = models.ManyToManyField(to=photo, blank=True)
    QR = models.CharField(max_length=1024, default='')
    venue = models.ForeignKey(Venue)

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField('email address', unique=True, db_index=True)
    #password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey(City)
    joined = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.NullBooleanField(default=False)
    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

class VenueAdministrator(models.Model):
    email =models.EmailField(max_length=254, blank= False, null= False, verbose_name="E-Mail")
    password = models.CharField(max_length=255, blank= False, null= False, verbose_name="Password")
    #password = hash(password)
    venue = models.ForeignKey(Venue, null= False, blank= False, verbose_name="Venue")
    active = models.NullBooleanField(blank=True, null= True)

class justTest(models.Model):
    record = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='images',blank=True , null=True)
    def __unicode__(self):
        return self.record