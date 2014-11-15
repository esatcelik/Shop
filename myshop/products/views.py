from django.shortcuts import render_to_response
from products.models import Bows, Arrows, Accessories


def bows(request):
    return render_to_response('products.html',
                             {'products':Bows.objects.all(),'mod':'bows','user':request.user})

def arrows(request):
    return render_to_response('products.html',
                             {'products':Arrows.objects.all(),'mod':'arrows','user':request.user})

def accessories(request):
    return render_to_response('products.html',
                             {'products':Accessories.objects.all(),'mod':'accessories','user':request.user})

def bow(request, product_id=1):
    return render_to_response('product.html',
                              {'product':Bows.objects.get(id=product_id),'user':request.user})
    
def arrow(request, product_id=1):
    return render_to_response('product.html',
                              {'product':Arrows.objects.get(id=product_id),'user':request.user})
    
def accessory(request, product_id=1):
    return render_to_response('product.html',
                              {'product':Accessories.objects.get(id=product_id),'user':request.user})