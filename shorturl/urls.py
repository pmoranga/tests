from django.conf.urls.defaults import *

from shorturl.surl.models import URL

info_dict = {
    'queryset': URL.objects.all(),
}

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    (r'^$', 'shorturl.surl.views.index'),
    (r'^(?P<url_id>[^/]{6})$','shorturl.surl.views.open_surl'),
    # Example:
    # (r'^shorturl/', include('shorturl.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
