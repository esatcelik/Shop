from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^bows/sub/(?P<type>.+)/$','products.views.bows'),
    url(r'^arrows/sub/(?P<type>.+)/$','products.views.arrows'),
    url(r'^accessories/sub/(?P<type>.+)/$','products.views.accessories'),
    
    url(r'^bows/$','products.views.bows'),
    url(r'^arrows/$','products.views.arrows'),
    url(r'^accessories/$','products.views.accessories'),
 
    url(r'^bows/get/(?P<product_id>\d+)/$', 'products.views.bow'),
    url(r'^arrows/get/(?P<product_id>\d+)/$', 'products.views.arrow'),
    url(r'^accessories/get/(?P<product_id>\d+)/$', 'products.views.accessory'),
    
    
    )