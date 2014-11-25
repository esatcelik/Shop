from django.shortcuts import render_to_response
from django.template import RequestContext
from products.models import Bows, Arrows, Accessories

# Create your views here.
def main(request):
    b = Bows.objects.order_by('-pk')[:4]  # @UndefinedVariable
    ar = Arrows.objects.order_by('-pk')[:4]  # @UndefinedVariable
    ac = Accessories.objects.order_by('-pk')[:4]  # @UndefinedVariable
    return render_to_response('index.html', RequestContext(request, {'user':request.user,'bows':b,'arrows':ar,'accessories':ac}))

def contact(request):
    return render_to_response('contact.html', RequestContext(request, {'user':request.user}))
