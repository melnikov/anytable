# coding=utf-8
from django.contrib import admin
from imagekit.admin import AdminThumbnail
from image_cropping import ImageCroppingMixin

# Register your models here.
from anytable_v1.models import *


class testUsersAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName',)

class EventThePrice(admin.TabularInline):
    model = EventPrice
    extra = 1

class eventAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'event_date', 'venue', 'thumbnail',)
    inlines = [ EventThePrice, ]
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

class PriceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class VenueAdministratorPanel(admin.ModelAdmin):
    #exclude = ["password", ]
    list_display = ("email", "password", )

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "password")

class DocumentsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = (  "thumbnail", "title",)
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')

class FolderAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")

#admin.site.register(photo, photoAdmin)
admin.site.register(VenueOptions, venueOptionAdmin)
admin.site.register(VenueKitchen,venueKitchenAdmin)
admin.site.register(TestUsers,testUsersAdmin)
admin.site.register(Subscriber, subscriberAdmin)
admin.site.register(VenueType, typeAdmin)

admin.site.register(Venue, venueAdmin)
admin.site.register(Event, eventAdmin)
admin.site.register(Region, regionAdmin)
admin.site.register(City, cityAdmin)
admin.site.register(VenueAdministrator, VenueAdministratorPanel)
admin.site.register(Document, DocumentsAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(PriceType, PriceTypeAdmin)
admin.site.register(Customer, CustomerAdmin)


