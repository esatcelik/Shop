from django.shortcuts import render_to_response
from products.models import Bows, Arrows, Accessories
from django.core.context_processors import csrf
from django.template import RequestContext
from django.db.models import Q

def bows(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('products.html',
                             {'products':Bows.objects.filter(~Q(quantity = 0)),'mod':'bows','user':request.user},RequestContext(request,c))  # @UndefinedVariable

def arrows(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('products.html',
                             {'products':Arrows.objects.filter(~Q(quantity = 0)),'mod':'arrows','user':request.user},RequestContext(request,c))  # @UndefinedVariable

def accessories(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('products.html',
                             {'products':Accessories.objects.filter(~Q(quantity = 0)),'mod':'accessories','user':request.user},RequestContext(request,c))  # @UndefinedVariable

def bow(request, product_id=1):
    c = {}
    c.update(csrf(request))
    return render_to_response('product.html',
                              {'product':Bows.objects.get(id=product_id),'mod':'bows','user':request.user},RequestContext(request,c))
    
def arrow(request, product_id=1):
    c = {}
    c.update(csrf(request))
    return render_to_response('product.html',
                              {'product':Arrows.objects.get(id=product_id),'mod':'arrows','user':request.user},RequestContext(request,c))
    
def accessory(request, product_id=1):
    c = {}
    c.update(csrf(request))
    return render_to_response('product.html',
                              {'product':Accessories.objects.get(id=product_id),'mod':'accessories','user':request.user},RequestContext(request,c))