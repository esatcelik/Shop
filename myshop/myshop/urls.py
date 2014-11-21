from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static, settings

urlpatterns = patterns('',

    url(r'^$', 'home.views.main'),
    url(r'^contact$', 'home.views.contact'),
    url(r'^products/',include('products.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
    url(r'^cart/',include('shopcart.urls')),
    url(r'^check/',include('checkout.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)