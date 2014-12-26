from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^out/$','checkout.views.out'),
    url(r'^review/$','checkout.views.review'),
    url(r'^review2/$','checkout.views.review2'),
    url(r'^delete/$','checkout.views.delete'),
     )