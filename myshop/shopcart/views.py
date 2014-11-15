from django.shortcuts import render_to_response
from shopcart.models import Cart

# Create your views here.
def add(request):
    
    user_id2 = request.POST.get('u_id', '')
    mod = request.POST.get('mod', '')
    product_id2 = request.POST.get('p_id', '')
    bow_id2 = ""
    arrow_id2 = ""
    accessory_id2 = ""
    if mod == "bows":
        bow_id2 = product_id2
    if mod == "arrows":
        arrow_id2 = product_id2
    if mod == "accessories":
        accessory_id2 = product_id2
        
    data=Cart(user_id1=user_id2,bow_id1=bow_id2,arrow_id1=arrow_id2,accessory_id1=accessory_id2)
    data.save()
    return render_to_response('cart.html',
                             {'user':request.user})



def show(request):

    return render_to_response('cart.html',
                             {'user':request.user})