from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$','products.views.products'),
    url(r'^get/(?P<product_id>\d+)/$', 'products.views.product'),
    )