from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from products.models import Bows, Arrows, Accessories
from checkout.models import Check, Package
from shopcart.models import Cart
from django.shortcuts import redirect
from django.core.context_processors import csrf
from django.template import RequestContext
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
    
    a = Check(bow_data=bow, arrow_data=arrow, accessory_data=accessories, user_id1=user_id1, Tprice=total, used=0)
    a.save()
    
    
    
    f = Check.objects.filter(user_id1=request.user.id, used=0)  # @UndefinedVariable
    
    for j in f:
        a1 = 0
        d = j.Tprice
        
        b1 = eval(j.bow_data).values()
        for i in b1:
            a1 = a1 + int(i)
        b1 = eval(j.arrow_data).values()
        for i in b1:
            a1 = a1 + int(i)
        b1 = eval(j.accessory_data).values()
        for i in b1:
            a1 = a1 + int(i)
        j.used=1
        j.save()
        g = Package(user_id1=j.user_id1, Tprice=d, quantity=a1, real_id = j.id)
        g.save()
    
    
    return redirect('checkout.views.review')

def review(request):
    c = {}
    c.update(csrf(request))
    f = Package.objects.filter(user_id1=request.user.id)  # @UndefinedVariable

    return render_to_response('checkout.html',
                             {'user':request.user, 'data':f},RequestContext(request,c))

def delete(request):
    c = {}
    c.update(csrf(request))
    
    l = request.POST.get('c_id', '')
    l2 = request.POST.get('pac_id', '')
    
    f1 = Package.objects.get(id=l2)
    f1.delete()

    f = Check.objects.get(id=l)
    
    a= eval(f.arrow_data)
    
    d= a.keys()
    for i in d:
        r = Arrows.objects.get(id = int(i))
        r.quantity = r.quantity + int(a[i])
        r.save()
    
    a= eval(f.bow_data)
    
    d= a.keys()
    for i in d:
        r = Bows.objects.get(id = int(i))
        r.quantity = r.quantity + int(a[i])
        r.save()
    
    a= eval(f.accessory_data)
    
    d= a.keys()
    for i in d:
        r = Accessories.objects.get(id = int(i))
        r.quantity = r.quantity + int(a[i])
        r.save()
  
    return redirect('checkout.views.review')