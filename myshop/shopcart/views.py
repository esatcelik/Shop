from django.shortcuts import render_to_response
from shopcart.models import Cart
from products.models import Bows, Arrows, Accessories
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import redirect

# Create your views here.
def add(request):
    
    c = {}
    c.update(csrf(request))
    
    user_id2 = request.POST.get('u_id', '')
    mod = request.POST.get('mod', '')
    product_id2 = request.POST.get('p_id', '')

    if not Cart.objects.filter(user_id1=user_id2).exists():  # @UndefinedVariable
        d = {'bows':[],'arrows':[],'accessories':[]}
        d = str(d)
        dat=Cart(user_id1=user_id2,data=d)
        dat.save()
        a = eval(dat.data)
        a[mod].append(product_id2)
        a[mod]=list(set(a[mod]))
        d=str(a)
        dat.data=d
        dat.save()
    else:
        dat = Cart.objects.get(user_id1=user_id2) # @UndefinedVariable
        d = eval(dat.data)
        d[mod].append(product_id2)
        d[mod]=list(set(d[mod]))
        d=str(d)
        dat.data=d
        dat.save()
    
    return redirect('shopcart.views.show')

def delete(request):
    c = {}
    c.update(csrf(request))
    
    p_id = request.POST.get('p_id', '')
    if 'bow1' in request.POST:
        dat = Cart.objects.get(user_id1=request.user.id)
        d = eval(dat.data)
        d['bows'].remove(p_id)
    if 'arrow1' in request.POST:
        dat = Cart.objects.get(user_id1=request.user.id)
        d = eval(dat.data)
        d['arrows'].remove(p_id)
    if 'accessory1' in request.POST:
        dat = Cart.objects.get(user_id1=request.user.id)
        d = eval(dat.data)
        d['accessories'].remove(p_id)
    
    dat.data=str(d)
    dat.save()
    
    return redirect('shopcart.views.show')

def show(request):
    c = {}
    c.update(csrf(request))
    try:
        dat = Cart.objects.get(user_id1=request.user.id)
        d = eval(dat.data)
    except Cart.DoesNotExist:
        return render_to_response('cart.html',
                             {'user':request.user},RequestContext(request,c))
    
    
    
    try:
        bow = Bows.objects.filter(id__in = d['bows'])  # @UndefinedVariable
    except Bows.DoesNotExist:
        bow = None
    
    try:
        arrow = Arrows.objects.filter(id__in = d['arrows'])  # @UndefinedVariable
    except Arrows.DoesNotExist:
        arrow = None
    
    try:
        accessories = Accessories.objects.filter(id__in = d['accessories'])  # @UndefinedVariable
    except Accessories.DoesNotExist:
        accessories = None

    return render_to_response('cart.html',
                             {'user':request.user,'bow':bow,'arrow':arrow,'accessories':accessories},RequestContext(request,c))