from django.shortcuts import render_to_response
from products.models import Bows, Arrows, Accessories
from django.core.context_processors import csrf
from django.template import RequestContext
from django.db.models import Q
from reviews.models import Reviews

def bows(request, type=None):
    
    low_range = request.POST.get('1', '')
    upp_range = request.POST.get('2', '')
    
    if low_range == "":
        low_range = 0
    if upp_range == "":
        upp_range = 9999999
    
    if request.POST:
        low_range = int(low_range)  # @UndefinedVariable
        upp_range = int(upp_range)  # @UndefinedVariable
    else:
        low_range=0
        upp_range=9999999

    c = {}
    c.update(csrf(request))
    
    if type==None:
        a = Bows.objects.filter(~Q(quantity = 0) & Q(price__range=(low_range,upp_range)))  # @UndefinedVariable
        up = ""
    else:
        a = Bows.objects.filter(~Q(quantity = 0) & Q(price__range=(low_range,upp_range)) & Q(type=type))  # @UndefinedVariable
        up = "../"
    
    
    
    return render_to_response('products.html',
                             {'products':a,'mod':'bows','up':up,'user':request.user},RequestContext(request,c))  # @UndefinedVariable

def arrows(request, type=None):
    low_range = request.POST.get('1', '')
    upp_range = request.POST.get('2', '')
    
    if low_range == "":
        low_range = 0
    if upp_range == "":
        upp_range = 9999999
    
    if request.POST:
        low_range = int(low_range)  # @UndefinedVariable
        upp_range = int(upp_range)  # @UndefinedVariable
    else:
        low_range=0
        upp_range=9999999
    
    c = {}
    c.update(csrf(request))
    
    if type==None:
        a = Arrows.objects.filter(~Q(quantity = 0) & Q(price__range=(low_range,upp_range)))  # @UndefinedVariable
        up = ""
    else:
        a = Arrows.objects.filter(~Q(quantity = 0) & Q(price__range=(low_range,upp_range)) & Q(type=type))  # @UndefinedVariable
        up = "../"
        
    return render_to_response('products.html',
                             {'products':a,'up':up,'mod':'arrows','user':request.user},RequestContext(request,c))  # @UndefinedVariable

def accessories(request, type=None):
    low_range = request.POST.get('1', '')
    upp_range = request.POST.get('2', '')
    
    if low_range == "":
        low_range = 0
    if upp_range == "":
        upp_range = 9999999
    
    if request.POST:
        low_range = int(low_range)  # @UndefinedVariable
        upp_range = int(upp_range)  # @UndefinedVariable
    else:
        low_range=0
        upp_range=9999999
    
    c = {}
    c.update(csrf(request))

    if type==None:
        a = Accessories.objects.filter(~Q(quantity = 0) & Q(price__range=(low_range,upp_range)))  # @UndefinedVariable
        up = ""
    else:
        a = Accessories.objects.filter(~Q(quantity = 0) & Q(price__range=(low_range,upp_range)) & Q(type=type))  # @UndefinedVariable
        up = "../"


    return render_to_response('products.html',
                             {'products':a,'up':up,'mod':'accessories','user':request.user},RequestContext(request,c))  # @UndefinedVariable

def bow(request, product_id=1):
    c = {}
    c.update(csrf(request))
    
    rev = Reviews.objects.filter(Q(pro_id=product_id) & Q(mod='bows'))  # @UndefinedVariable
    
    return render_to_response('product.html',
                              {'product':Bows.objects.get(id=product_id),'reviews':rev,'mod':'bows','user':request.user},RequestContext(request,c))
    
def arrow(request, product_id=1):
    c = {}
    c.update(csrf(request))
     
    rev = Reviews.objects.filter(Q(pro_id=product_id) & Q(mod='arrows'))  # @UndefinedVariable
    
    return render_to_response('product.html',
                              {'product':Arrows.objects.get(id=product_id),'reviews':rev,'mod':'arrows','user':request.user},RequestContext(request,c))
    
def accessory(request, product_id=1):
    c = {}
    c.update(csrf(request))
    
    rev = Reviews.objects.filter(Q(pro_id=product_id) & Q(mod='accessories'))  # @UndefinedVariable
    
    return render_to_response('product.html',
                              {'product':Accessories.objects.get(id=product_id),'reviews':rev,'mod':'accessories','user':request.user},RequestContext(request,c))
