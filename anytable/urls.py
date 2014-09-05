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
    url(r'^query/admin/addvenueimg/', 'anytable_v1.admin_views.AddVenueImg', name='Add Venue Image'),

    #Non-Admin
    url(r'^$','anytable_v1.views.index',name='index'),
    url(r'^test/', 'anytable_v1.views.test', name='test'),
    # url(r'^ajax/front/(?P<type>[a-zA-Z0-9_][0-9a-zA-Z_]*/$)', 'anytable_v1.views.ajaxFront', name='Ajax For Front Page'),
    url(r'^query/type/(?P<type>[a-zA-Z0-9_][0-9a-zA-Z_]*/$)', 'anytable_v1.views.ajaxFront', name='Queries For Front Page'),
    url(r'^venue/(?P<id>[0-9]+)', 'anytable_v1.views.venueCard', name='Venue Card'),
    url(r'^search/$', 'anytable_v1.views.searchResult', name='Search Results'),
)
