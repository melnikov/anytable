from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anytable.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','anytable_v1.views.index',name='index'),
    url(r'^test/', 'anytable_v1.views.test', name='test'),
    # url(r'^ajax/front/(?P<type>[a-zA-Z0-9_][0-9a-zA-Z_]*/$)', 'anytable_v1.views.ajaxFront', name='Ajax For Front Page'),
    url(r'^query/type/(?P<type>[a-zA-Z0-9_][0-9a-zA-Z_]*/$)', 'anytable_v1.views.ajaxFront', name='Queries For Front Page'),
    url(r'^venue/(?P<id>[0-9]+)', 'anytable_v1.views.venueCard', name='Venue Card'),
)
