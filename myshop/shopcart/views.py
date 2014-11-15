from django.shortcuts import render_to_response
from shopcart.models import Cart

# Create your views here.

def show(request):

    return render_to_response('cart.html',
                             {'user':request.user})