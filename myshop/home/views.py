from django.shortcuts import render_to_response
from django.template import RequestContext
from products.models import Bows, Arrows, Accessories
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


def main(request):
    b = Bows.objects.order_by('-pk')[:4]  # @UndefinedVariable
    ar = Arrows.objects.order_by('-pk')[:4]  # @UndefinedVariable
    ac = Accessories.objects.order_by('-pk')[:4]  # @UndefinedVariable
    return render_to_response('index.html', RequestContext(request, {'user':request.user,'bows':b,'arrows':ar,'accessories':ac}))

def contact(request):
    return render_to_response('contact.html', RequestContext(request, {'user':request.user}))


@csrf_exempt
def signup(request):
    
    username = request.POST.get('user', '')
    pass1 = request.POST.get('pass', '')
    pass2 = request.POST.get('pass2', '')
    
    if pass1 != pass2:
        return redirect('../../accounts/login')
    
    
    user = User.objects.create_user(username, 'email@email.com', pass1)
    user.save()
    
    return redirect('home.views.main')
    