from django.shortcuts import render_to_response
from products.models import Products, Bows, Arrows, Accessories

def products(request):
    return render_to_response('products.html',
                             {'products':Products.objects.all()})

def product(request, product_id=1):
    return render_to_response('product.html',
                              {'product':Products.objects.get(id=product_id)})

def bows(request):
    return render_to_response('products.html',
                             {'bows':Bows.objects.all()})

def arrows(request):
    return render_to_response('products.html',
                             {'arrows':Arrows.objects.all()})

def accessories(request):
    return render_to_response('products.html',
                             {'accessories':Accessories.objects.all()})