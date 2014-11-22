from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^out/$','checkout.views.out'),
    url(r'^review/$','checkout.views.review'),
    url(r'^delete/$','checkout.views.delete'),
     )