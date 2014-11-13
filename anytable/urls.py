from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anytable.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Admin Stuff
    url(r'^admin/', include(admin.site.urls)),
    url(r'^query/admin/ven_admin_logout', 'anytable_v1.admin_views.ven_admin_logout', name='Venue Admin Logout'),
    url(r'^query/admin/venueadministratorauth/', 'anytable_v1.admin_views.venueadministratorauth', name='Venue Admin Auth'),
    url(r'^venueadministrator/' , 'anytable_v1.admin_views.TheVenueAdministration', name='TheVenueAdministration'),

    url(r'^query/admin/deleteimg/(?P<id>[0-9]+)', 'anytable_v1.admin_views.DeleteVenueImg', name='delete venue image'),
    #url(r'^query/admin/addvenueimg/(?P<id>[0-9]+)/(?P<FILES>)', 'anytable_v1.admin_views.AddVenueImg', name='Add Venue Image'),
    #url(r'^query/admin/addvenueimg/(?P<id>[0-9]+)', 'anytable_v1.admin_views.AddVenueImg', name='Add Venue Image'),
    #url(r'^query/admin/addvenueimg/', 'anytable_v1.admin_views.AddVenueImg', name='Add Venue Image'),
##Venue Control, Venue Administration ..
     url(r'^venueaddimg/$', 'anytable_v1.admin_views.venueaddimg', name='Venue Add Img'),
     url(r'^venueupdatelogo/$', 'anytable_v1.admin_views.venueupdatelogo', name='Venue Update Logo'),
     url(r'^query/admin/update_venue_telephone/', 'anytable_v1.admin_views.update_venue_telephone', name='Update Venue Telephone'),
     url(r'^query/admin/update_venue_email/', 'anytable_v1.admin_views.update_venue_email', name='Update Venue Email'),
     url(r'^query/admin/update_venue_workregime/', 'anytable_v1.admin_views.update_venue_workregime', name='Update Venue workregime'),
     url(r'^query/admin/updatevenuesite/', 'anytable_v1.admin_views.updatevenuesite', name='Update Venue Site'),
     url(r'^query/admin/updatevenuefb/', 'anytable_v1.admin_views.updatevenuefb', name='Update Venue Facebook'),
     url(r'^query/admin/updatevenuetwitter/', 'anytable_v1.admin_views.updatevenuetwitter', name='Update Venue Twitter'),
     url(r'^query/admin/updatevenueinstagram/', 'anytable_v1.admin_views.updatevenueinstagram', name='Update Venue Instagram'),
     url(r'^query/admin/updatevenuevk/', 'anytable_v1.admin_views.updatevenuevk', name='Update Venue VK'),
     url(r'^query/admin/updatevenuedescription/', 'anytable_v1.admin_views.updatevenuedescription', name='Update Description'),
     url(r'^query/admin/update_venue_options/', 'anytable_v1.admin_views.update_venue_options', name='Update Venue Options'),
     url(r'^query/admin/update_venue_kitchen/', 'anytable_v1.admin_views.update_venue_kitchen', name='Update Venue Kitchen'),
     url(r'^query/admin/update_venue_type/', 'anytable_v1.admin_views.update_venue_type', name='Update Venue Type'),

## Events Control, Venue Administration..
     url(r'^addevent/$', 'anytable_v1.admin_views.addevent', name='Add Event'),
     url(r'^query/admin/delete_event/', 'anytable_v1.admin_views.delete_event', name='Delete Event'),
     url(r'^query/admin/update_event/', 'anytable_v1.admin_views.update_event', name='Update Event'),
     url(r'^query/admin/update_event_img/', 'anytable_v1.admin_views.update_event_img', name= 'Update Event Img'),
     url(r'^query/admin/update_event_price/', 'anytable_v1.admin_views.update_event_price', name= 'Update Event Price'),
     url(r'^query/admin/refresh_event_prices/', 'anytable_v1.admin_views.refresh_event_prices', name= 'Refresh Event Price'),
     url(r'^query/admin/delete_event_price/', 'anytable_v1.admin_views.delete_event_price', name= 'Delete Event Price'),

## Customers
     url(r'^customer/profile/', 'anytable_v1.customer_views.profile', name= 'Customer profile'),
     url(r'^customer/register/', 'anytable_v1.customer_views.register', name= 'Customer register'),
     url(r'^customer/login/', 'anytable_v1.customer_views.login', name= 'Customer Login'),
     url(r'^customer/customer_auth/', 'anytable_v1.customer_views.customer_auth', name= 'Customer Authentication'),
     url(r'^customer/cusImg/', 'anytable_v1.customer_views.cusImg', name='Customer Img Edit'),
     url(r'^customer/cusPhone/', 'anytable_v1.customer_views.cusPhone', name='Customer Phone Edit'),
     url(r'^customer/cusEmail/', 'anytable_v1.customer_views.cusEmail', name='Customer Email Edit'),
     url(r'^customer/cusFacebook/', 'anytable_v1.customer_views.cusFacebook', name='Customer Facebook Edit'),
     url(r'^customer/cusInstagram/', 'anytable_v1.customer_views.cusInstagram', name='Customer Instagram Edit'),
     url(r'^customer/cusTwitter/', 'anytable_v1.customer_views.cusTwitter', name='Customer Twitter Edit'),
     url(r'^customer/cusVk/', 'anytable_v1.customer_views.cusVk', name='Customer Vk Edit'),
     url(r'^customer/cuslogOut/', 'anytable_v1.customer_views.cuslogOut', name='Customer Logout'),

##Non-Admin
     url(r'^$','anytable_v1.views.index',name='index'),
     url(r'^test/', 'anytable_v1.views.test', name='test'),
    # url(r'^ajax/front/(?P<type>[a-zA-Z0-9_][0-9a-zA-Z_]*/$)', 'anytable_v1.views.ajaxFront', name='Ajax For Front Page'),
     url(r'^query/type/(?P<type>[a-zA-Z0-9_][0-9a-zA-Z_]*/$)', 'anytable_v1.views.ajaxFront', name='Queries For Front Page'),
     url(r'^venue/(?P<id>[0-9]+)', 'anytable_v1.views.venueCard', name='Venue Card'),
     url(r'^search/$', 'anytable_v1.views.searchResult', name='Search Results'),
     url(r'^event_prices/', 'anytable_v1.views.event_prices', name='Event Prices, Main'),
)
