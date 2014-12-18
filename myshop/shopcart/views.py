from django.shortcuts import render_to_response
from shopcart.models import Cart
from products.models import Bows, Arrows, Accessories
from recommendation.models import Rec
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import redirect

def rec_cal():
    
    return  0

def add(request):
    
    
    
    c = {}
    c.update(csrf(request))
    
    user_id2 = request.POST.get('u_id', '')
    mod = request.POST.get('mod', '')
    product_id2 = request.POST.get('p_id', '')
    
    if not Rec.objects.filter(user1_id=user_id2).exists():  # @UndefinedVariable
        print "a"
        a=Rec(user1_id=user_id2,rec_bow=str([]),rec_arrow=str([]),rec_accessory=str([]))  # @UndefinedVariable
        a.save()

    
    rec1 = Rec.objects.get(user1_id=user_id2)  # @UndefinedVariable
        
    if mod == "bows":
        d = eval(rec1.rec_bow)  # @UndefinedVariable
        d.append(int(product_id2))  # @UndefinedVariable
        rec1.rec_bow = str(d)  # @UndefinedVariable
        rec1.save()
                            
    if mod == "arrows":
        d = eval(rec1.rec_arrow)  # @UndefinedVariable
        d.append(int(product_id2))  # @UndefinedVariable
        rec1.rec_arrow = str(d)  # @UndefinedVariable
        rec1.save()
        
    if mod == "accessories":
        d = eval(rec1.rec_accessory)  # @UndefinedVariable
        d.append(int(product_id2))  # @UndefinedVariable
        rec1.rec_accessory = str(d)  # @UndefinedVariable
        rec1.save()
    
    if not Cart.objects.filter(user_id1=user_id2).exists():  # @UndefinedVariable
        d = {'bows':[],'arrows':[],'accessories':[]}
        d = str(d)  # @UndefinedVariable
        dat=Cart(user_id1=user_id2,data=d)
        dat.save()
        a = eval(dat.data)  # @UndefinedVariable
        a[mod].append(product_id2)
        a[mod]=list(set(a[mod]))  # @UndefinedVariable
        d=str(a)  # @UndefinedVariable
        dat.data=d
        dat.save()
    else:
        dat = Cart.objects.get(user_id1=user_id2) # @UndefinedVariable
        d = eval(dat.data)  # @UndefinedVariable
        d[mod].append(product_id2)
        d[mod]=list(set(d[mod]))  # @UndefinedVariable
        d=str(d)  # @UndefinedVariable
        dat.data=d
        dat.save()
    
    return redirect('shopcart.views.show')

def delete(request):
    c = {}
    c.update(csrf(request))
    
    p_id = request.POST.get('p_id', '')
    if 'bow1' in request.POST:
        dat = Cart.objects.get(user_id1=request.user.id)
        d = eval(dat.data)  # @UndefinedVariable
        d['bows'].remove(p_id)
    if 'arrow1' in request.POST:
        dat = Cart.objects.get(user_id1=request.user.id)
        d = eval(dat.data)  # @UndefinedVariable
        d['arrows'].remove(p_id)
    if 'accessory1' in request.POST:
        dat = Cart.objects.get(user_id1=request.user.id)
        d = eval(dat.data)  # @UndefinedVariable
        d['accessories'].remove(p_id)
    
    dat.data=str(d)  # @UndefinedVariable
    dat.save()
    
    return redirect('shopcart.views.show')

def show(request):
    c = {}
    c.update(csrf(request))
    try:
        dat = Cart.objects.get(user_id1=request.user.id)
        d = eval(dat.data)  # @UndefinedVariable
    except Cart.DoesNotExist:
        return render_to_response('cart.html',
                             {'user':request.user},RequestContext(request,c))
    
    
    
    try:
        bow = Bows.objects.filter(id__in = d['bows'])  # @UndefinedVariable
    except Bows.DoesNotExist:
        bow = None  # @UndefinedVariable
    
    try:
        arrow = Arrows.objects.filter(id__in = d['arrows'])  # @UndefinedVariable
    except Arrows.DoesNotExist:
        arrow = None  # @UndefinedVariable
    
    try:
        accessories = Accessories.objects.filter(id__in = d['accessories'])  # @UndefinedVariable
    except Accessories.DoesNotExist:
        accessories = None  # @UndefinedVariable

    return render_to_response('cart.html',
                             {'user':request.user,'bow':bow,'arrow':arrow,'accessories':accessories},RequestContext(request,c))