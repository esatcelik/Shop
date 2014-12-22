from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.shortcuts import redirect
from reviews.models import Reviews
from products.models import Bows, Arrows, Accessories
from django.template import RequestContext
from django.contrib.auth.models import User


def add(request):
    
    c = {}
    c.update(csrf(request))
    
    username1 = request.POST.get('user', '')
    pro_id1 = request.POST.get('id', '')
    review1 = request.POST.get('review', '')
    mod1 = request.POST.get('mod', '')

    a = Reviews(pro_id=pro_id1,review=review1,username=username1,mod=mod1)
    a.save()


    return redirect('/products/%s/get/%s/' % (mod1, pro_id1),RequestContext(request,c))
    
