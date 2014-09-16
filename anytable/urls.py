from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anytable.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Admin Stuff
    url(r'^admin/anytable_v1/venueadministrator/(?P<id>[0-9]+)/$' , 'anytable_v1.admin_views.TheVenueAdministration', name='TheVenueAdministration'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^query/admin/deleteimg/(?P<id>[0-9]+)', 'anytable_v1.admin_views.DeleteVenueImg', name='delete venue image'),
    #url(r'^query/admin/addvenueimg/(?P<id>[0-9]+)/(?P<FILES>)', 'anytable_v1.admin_views.AddVenueImg', name='Add Venue Image'),
    #url(r'^query/admin/addvenueimg/(?P<id>[0-9]+)', 'anytable_v1.admin_views.AddVenueImg', name='Add Venue Image'),
    #url(r'^query/admin/addvenueimg/', 'anytable_v1.admin_views.AddVenueImg', name='Add Venue Image'),
##Venue Control, Venue Administration ..
     url(r'^venueaddimg/$', 'anytable_v1.admin_views.venueaddimg', name='Venue Add Img'),
     url(r'^venueupdatelogo/$', 'anytable_v1.admin_views.venueupdatelogo', name='Venue Update Logo'),
     url(r'^query/admin/updatevenueemail/', 'anytable_v1.admin_views.updatevenueemail', name='Update Venue Email'),
     url(r'^query/admin/updatevenuesite/', 'anytable_v1.admin_views.updatevenuesite', name='Update Venue Site'),
     url(r'^query/admin/updatevenuefb/', 'anytable_v1.admin_views.updatevenuefb', name='Update Venue Facebook'),
     url(r'^query/admin/updatevenuetwitter/', 'anytable_v1.admin_views.updatevenuetwitter', name='Update Venue Twitter'),
     url(r'^query/admin/updatevenueinstagram/', 'anytable_v1.admin_views.updatevenueinstagram', name='Update Venue Instagram'),
     url(r'^query/admin/updatevenuevk/', 'anytable_v1.admin_views.updatevenuevk', name='Update Venue VK'),
     url(r'^query/admin/updatevenuedescription/', 'anytable_v1.admin_views.updatevenuedescription', name='Update Description'),

## Events Control, Venue Administration..
     url(r'^addevent/$', 'anytable_v1.admin_views.addevent', name='Add Event'),
     url(r'^query/admin/deleteevent/', 'anytable_v1.admin_views.deleteevent', name='Delete Event'),
     url(r'^query/admin/updateevent/', 'anytable_v1.admin_views.updateevent', name='Update Event'),
     url(r'^query/admin/updateeventimg/', 'anytable_v1.admin_views.updateeventimg', name= 'Update Event Img'),

##Non-Admin
     url(r'^$','anytable_v1.views.index',name='index'),
     url(r'^test/', 'anytable_v1.views.test', name='test'),
    # url(r'^ajax/front/(?P<type>[a-zA-Z0-9_][0-9a-zA-Z_]*/$)', 'anytable_v1.views.ajaxFront', name='Ajax For Front Page'),
     url(r'^query/type/(?P<type>[a-zA-Z0-9_][0-9a-zA-Z_]*/$)', 'anytable_v1.views.ajaxFront', name='Queries For Front Page'),
     url(r'^venue/(?P<id>[0-9]+)', 'anytable_v1.views.venueCard', name='Venue Card'),
     url(r'^search/$', 'anytable_v1.views.searchResult', name='Search Results'),
)
