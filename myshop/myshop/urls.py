from shop import urls as shop_urls
from django.conf.urls import patterns, include
from django.contrib import admin

urlpatterns = patterns('',
    # Example:
    #(r'^example/', include('example.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^shop/', include(shop_urls)), # <-- That's the important bit
    # You can obviously mount this somewhere else
)