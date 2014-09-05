# coding=utf-8
from django.contrib import admin
from imagekit.admin import AdminThumbnail
from image_cropping import ImageCroppingMixin

# Register your models here.
from anytable_v1.models import *


class testUsersAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName',)


class eventAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'event_date', 'venue', 'thumbnail',)
    pass
    thumbnail = AdminThumbnail(image_field='thumbnail',)
    readonly_fields = ['thumbnail']

class regionAdmin(admin.ModelAdmin):
    list_display = ('name', )

class cityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', )

class venueImage(admin.TabularInline):
    model = Venueimage
    extra = 1
    thumbnail = AdminThumbnail(image_field = 'thumbnail')
    readonly_fields = ['thumbnail']

class venueKitchenAdmin(admin.ModelAdmin):
    list_display = ("name",)

class venueOptionAdmin(admin.ModelAdmin):
    list_display = ("name",)

class venueAdmin(ImageCroppingMixin, admin.ModelAdmin):
   filter_horizontal = ("type", "kitchen", "option")
   list_display = (  "name", "address", "kitchen_list", "image", "option_list", "types_list", "admin_thumbnail",)
   inlines = [ venueImage, ]
   pass
   admin_thumbnail = AdminThumbnail(image_field='thumbnail')

class subscriberAdmin(admin.ModelAdmin):
    list_display = ("name", )

class typeAdmin(admin.ModelAdmin):
    list_display = ("name", )

class costumorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "telephone", "city", )
class VenueAdministratorPanel(admin.ModelAdmin):
    #exclude = ["password", ]
    list_display = ("email", "password", )
class JustTestAdmin(admin.ModelAdmin):
    list_display = ("record", "file", )
#admin.site.register(photo, photoAdmin)
admin.site.register(VenueOptions, venueOptionAdmin)
admin.site.register(VenueKitchen,venueKitchenAdmin)
admin.site.register(TestUsers,testUsersAdmin)
admin.site.register(Subscriber, subscriberAdmin)
admin.site.register(VenueType, typeAdmin)
admin.site.register(User, costumorAdmin)
admin.site.register(Venue, venueAdmin)
admin.site.register(Event, eventAdmin)
admin.site.register(Region, regionAdmin)
admin.site.register(City, cityAdmin)
admin.site.register(VenueAdministrator, VenueAdministratorPanel)
admin.site.register(justTest, JustTestAdmin)


