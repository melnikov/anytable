# coding=utf-8
from django.db import models
from south.modelsinspector import add_introspection_rules
from imagekit.models import ImageSpecField
from imagekit.processors import *
from image_cropping import ImageCropField, ImageRatioField
from pygeocoder import *
from django.contrib.auth.models import AbstractBaseUser
from django.forms import ModelForm
from django import forms
import hashlib
import _md5



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
    cropping = ImageRatioField('image', '220x170', free_crop=False)
    ##
    #logo_fe = ImageCropField(blank=True, null=True, upload_to='images')
    #cropping_fe = ImageRatioField('logo_fe', '220x170')
    ##
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})
    option = models.ManyToManyField(VenueOptions, null=True)
    subscriber = models.ForeignKey(Subscriber,null=True)
    #type = models.ForeignKey(venueType, null=True)
    type = models.ManyToManyField(VenueType, null=False)
    city = models.ForeignKey(City, null=True)
    address = models.TextField(blank=True, verbose_name="Address")
    facebook_url = models.CharField(max_length=1024, verbose_name="Facebook URL", blank=True, null=True)
    vk_url = models.CharField(max_length=1024, verbose_name="VK URL", blank=True, null=True)
    twitter = models.CharField(max_length=1024, verbose_name="Twitter", blank=True, null=True)
    instagram = models.CharField(max_length=1024, verbose_name="Instagram", blank=True, null=True)
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
    title = models.CharField(max_length=255 , default='event title',blank=False, null=False)
    image = models.ImageField(upload_to='images', blank=True,null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(325, 186)], format='JPEG', options={'quality': 60})
    date = models.DateTimeField( )
    event_date = models.DateField(blank=True,null=True)
    event_time = models.TimeField(blank=True,null=True)
    description = models.TextField(blank=True, verbose_name="Description")
    QR = models.CharField(max_length=1024, default='', blank=True,null=True)
    venue = models.ForeignKey(Venue)

class PriceType(models.Model):
    name = models.CharField(max_length=255, blank= False, null= False)
    def __unicode__(self):
       return u"%s " % self.name

class EventPrice(models.Model):
    price_type = models.ForeignKey(PriceType, blank=False, null=False)
    price = models.CharField(max_length=50, blank=True, null=True, verbose_name="Price")
    event = models.ForeignKey(Event, blank=False, verbose_name="Event")

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

def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

class VenueAdministrator(models.Model):
    email =models.EmailField(max_length=254, blank= False, null= False, verbose_name="E-Mail", unique=True)
    password = models.CharField(max_length=1024, blank= False, null= False, verbose_name="Password")
    venue = models.ForeignKey(Venue, null= False, blank= False, verbose_name="Venue")
    active = models.NullBooleanField(blank=True, null= True, )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.password = computeMD5hash(self.password)

        return super(VenueAdministrator,self).save(force_insert, force_update, using,
             update_fields)

class Customer(models.Model):
    name = models.CharField(max_length=1024, blank=False, null=False, verbose_name= 'Name')
    image = models.ImageField(upload_to='images', blank=True, null=True)
    email =models.EmailField(max_length=254, blank= False, null= False, verbose_name="E-Mail", unique=True)
    password = models.CharField(max_length=1024, blank= False, null= False, verbose_name="Password")
    phone = models.CharField(max_length=254, blank=True, null=True, verbose_name="Phone")
    facebook = models.CharField(max_length=1024, blank=True, verbose_name="facebook")
    twitter = models.CharField(max_length=1024, blank=True, verbose_name="twitter")
    instagram = models.CharField(max_length=1024, blank=True, verbose_name="instagram")
    vk = models.CharField(max_length=1024, blank=True, verbose_name="vk")
    active = models.NullBooleanField(blank=True, null= True, )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.password = computeMD5hash(self.password)

        return super(Customer,self).save(force_insert, force_update, using, update_fields)

class Document(models.Model):
    title = models.CharField(max_length=25, blank=True, null=True)

    docfile = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = ImageSpecField(source='docfile', processors=[ResizeToFit(325, 186)], format='JPEG', options={'quality': 60})

class Folder(models.Model):
    name = models.CharField(max_length=255, null=False)
    parent = models.ForeignKey('self',blank=True, null=True)
   # password = forms.PasswordInput('password', max_length=32, null=True)
    def __unicode__(self):
        return self.name

