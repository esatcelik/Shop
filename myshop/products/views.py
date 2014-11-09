from django.shortcuts import render_to_response
from products.models import Products

def products(request):
    return render_to_response('products.html',
                             {'products':Products.objects.all()})

def product(request, product_id=1):
    return render_to_response('product.html',
                              {'product':Products.objects.get(id=product_id)})

