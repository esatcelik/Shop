from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^show/$','shopcart.views.show'),
    url(r'^add/$','shopcart.views.add'),
    
     
     
     )