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
    model = venueimage
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

#admin.site.register(photo, photoAdmin)
admin.site.register(venueOptions, venueOptionAdmin)
admin.site.register(venueKitchen,venueKitchenAdmin)
admin.site.register(testUsers,testUsersAdmin)
admin.site.register(subscriber, subscriberAdmin)
admin.site.register(venueType, typeAdmin)
admin.site.register(user, costumorAdmin)
admin.site.register(venue, venueAdmin)
admin.site.register(event, eventAdmin)
admin.site.register(region, regionAdmin)
admin.site.register(city, cityAdmin)


