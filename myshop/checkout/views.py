from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from products.models import Bows, Arrows, Accessories
from checkout.models import Check
from shopcart.models import Cart
from django.shortcuts import redirect
from django.db import models
# Create your views here.


def clean(a):
    l=[]
    for i in a:
        if i == ",":
            pass
        else:
            l.append(i)
    l=''.join(l)
    d={}
    for i in range(1,len(l),2):
        d[l[i-1]]=l[i]
    return d

@csrf_exempt
def out(request):
    bow = request.POST.get('1', '')
    arrow = request.POST.get('2', '')
    accessories = request.POST.get('3', '')
    user_id1 = request.POST.get('4', '')
    total = 0
    bow = clean(bow)
    for i in bow.keys():
        bowObj= Bows.objects.get(id__in = i)
        bowObj.quantity = bowObj.quantity - int(bow[i])
        bowObj.save()
        total = total + (int(bow[i]) * bowObj.price)
        
    arrow = clean(arrow)
    for i in arrow.keys():
        arrowObj= Arrows.objects.get(id__in = i)
        arrowObj.quantity = arrowObj.quantity - int(arrow[i])
        arrowObj.save()
        total = total + (int(arrow[i]) * arrowObj.price)
    
    accessories = clean(accessories)
    for i in accessories.keys():
        accessoriesObj= Accessories.objects.get(id__in = i)
        accessoriesObj.quantity = accessoriesObj.quantity - int(accessories[i])
        accessoriesObj.save()
        total = total + (int(accessories[i]) * accessoriesObj.price)
    
    b = Cart.objects.get(user_id1=user_id1)
    b.delete()
    
    a = Check(bow_data=bow, arrow_data=arrow, accessory_data=accessories, user_id1=user_id1, Tprice=total)
    a.save()
    
    return redirect('checkout.views.review')

def review(request):
    
    f = Check.objects.filter(user_id1=request.user.id)  # @UndefinedVariable
    #c = {}
    #for d in f:
    #    d1 = d.bow_data
    #    d1 = eval(d1)
    #    for key,val in d1:
    #       a = Bows.objects.get(id=d[key])
    #       a.name
   
    
    
    
    
    return render_to_response('checkout.html',
                             {'user':request.user, 'data':f})