from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^$', 'home.views.main'),
    url(r'^products/',include('products.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
)
