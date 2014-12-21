from __future__ import division
from django.shortcuts import render_to_response
from shopcart.models import Cart
from products.models import Bows, Arrows, Accessories
from recommendation.models import Rec
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import redirect




def rec_cal(user_id2):
    
    sim = {}
    for user in Rec.objects.all():
        if user.user1_id == int(user_id2):  # @UndefinedVariable
            continue
        
        b = Rec.objects.get(user1_id=user.user1_id)
        
        a = Rec.objects.get(user1_id=int(user_id2))  # @UndefinedVariable
        
        a1 = eval(a.rec_bow)  # @UndefinedVariable
        b1 = eval(b.rec_bow)  # @UndefinedVariable
        
        sub_b = list(set(a1)-set(b1))  # @UnusedVariable @UndefinedVariable
        if len(sub_b) == 0:  # @UndefinedVariable
            continue
        s = len(a1)/len(sub_b)  # @UndefinedVariable
        print user.user1_id
        sim[user.user1_id] = s
        

        
        a1 = eval(a.rec_arrow)  # @UndefinedVariable
        b1 = eval(b.rec_arrow)  # @UndefinedVariable
        
        sub_a = list(set(a1)-set(b1))  # @UnusedVariable @UndefinedVariable
        if len(sub_a) == 0:  # @UndefinedVariable
            continue
        s = len(a1)/len(sub_a)  # @UndefinedVariable
        sim[user.user1_id] = sim[user.user1_id]*s

        
        a1 = eval(a.rec_accessory)  # @UndefinedVariable
        b1 = eval(b.rec_accessory)  # @UndefinedVariable
        
        sub_ac = list(set(a1)-set(b1))  # @UnusedVariable @UndefinedVariable
        if len(sub_ac) == 0:  # @UndefinedVariable
            continue
        s = len(a1)/len(sub_ac)  # @UndefinedVariable
        sim[user.user1_id] = sim[user.user1_id]*s
        
    return sim
    

def add(request):

    c = {}
    c.update(csrf(request))
    
    user_id2 = request.POST.get('u_id', '')
    mod = request.POST.get('mod', '')
    product_id2 = request.POST.get('p_id', '')
    
    if not Rec.objects.filter(user1_id=user_id2).exists():  # @UndefinedVariable

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