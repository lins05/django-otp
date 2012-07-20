from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from . import admin as otp_admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^otpadmin/', include(otp_admin.site.urls)),
)
