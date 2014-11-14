from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^all/$','products.views.products'),
    url(r'^bows/$','products.views.bows'),
    url(r'^arrows/$','products.views.arrows'),
    url(r'^accessories/$','products.views.accessories'),
    url(r'^get/(?P<product_id>\d+)/$', 'products.views.product'),
    )