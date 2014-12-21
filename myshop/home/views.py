import operator
from django.shortcuts import render_to_response
from django.template import RequestContext
from products.models import Bows, Arrows, Accessories
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from recommendation.models import Rec

def rec_cal(user_id2):
    
    sim = {}
    for user in Rec.objects.all():
        if user.user1_id == int(user_id2):  # @UndefinedVariable
            continue
        
        
        try:
            a = Rec.objects.get(user1_id=user.user1_id)
            a1 = eval(a.rec_bow)  # @UndefinedVariable
            
        except Rec.DoesNotExist:
            a1 = []
      
        try:
            b = Rec.objects.get(user1_id=int(user_id2))
            b1 = eval(b.rec_bow)  # @UndefinedVariable
            
        except Rec.DoesNotExist:
            b1 = []

       

        
        
        sub_b = list(set(a1)-set(b1))  # @UnusedVariable @UndefinedVariable
        if len(sub_b) == 0:  # @UndefinedVariable
            continue
        s = len(a1)/len(sub_b)  # @UndefinedVariable
        sim[user.user1_id] = s
        
        try:
            a = Rec.objects.get(user1_id=user.user1_id)
            a1 = eval(a.rec_arrow)  # @UndefinedVariable
            
        except Rec.DoesNotExist:
            a1 = []
      
        try:
            b = Rec.objects.get(user1_id=int(user_id2))
            b1 = eval(b.rec_arrow)  # @UndefinedVariable
            
        except Rec.DoesNotExist:
            b1 = []
        
        
        sub_a = list(set(a1)-set(b1))  # @UnusedVariable @UndefinedVariable
        if len(sub_a) == 0:  # @UndefinedVariable
            continue
        s = len(a1)/len(sub_a)  # @UndefinedVariable
        sim[user.user1_id] = sim[user.user1_id]*s

        try:
            a = Rec.objects.get(user1_id=user.user1_id)
            a1 = eval(a.rec_accessory)  # @UndefinedVariable
            
        except Rec.DoesNotExist:
            a1 = []
      
        try:
            b = Rec.objects.get(user1_id=int(user_id2))
            b1 = eval(b.rec_accessory)  # @UndefinedVariable
            
        except Rec.DoesNotExist:
            b1 = []
        
                
        sub_ac = list(set(a1)-set(b1))  # @UnusedVariable @UndefinedVariable
        if len(sub_ac) == 0:  # @UndefinedVariable
            continue
        s = len(a1)/len(sub_ac)  # @UndefinedVariable
        sim[user.user1_id] = sim[user.user1_id]*s

    x = sim
    
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    
    sorted_x.reverse()
    
    l=[]
    
    for i in range(len(sorted_x)):
        f = sorted_x[i]
        f = f[0]
        l.append(f)
 
    return l

def rec_result(user):
    
    sim_users = rec_cal(user)
    
    
    try:
        target_user = Rec.objects.get(user1_id=user)
   
    except Rec.DoesNotExist:
        return {}
    
    
    target_user = Rec.objects.get(user1_id=user)

    d = {'bow':[],'arrow':[],'accessory':[]}
    
    for sim_id in sim_users:
        sim_user = Rec.objects.get(user1_id=sim_id)
        bow1 = eval(sim_user.rec_bow)
        arrow1 = eval(sim_user.rec_arrow)
        accessory1 = eval(sim_user.rec_accessory)

        bow2 = eval(target_user.rec_bow)
        arrow2 = eval(target_user.rec_arrow)
        accessory2 = eval(target_user.rec_accessory)
        
        bow = list(set(bow1)-set(bow2))
        arrow = list(set(arrow1)-set(arrow2))
        accessory = list(set(accessory1)-set(accessory2))

        d['bow']=d['bow'] + bow
        d['arrow']=d['arrow'] + arrow
        d['accessory']=d['accessory'] + accessory
        

    return d


def main(request):
    
    if not request.user.is_authenticated():
        return redirect('accounts/login')
    
    b = Bows.objects.order_by('-pk')[:4]  # @UndefinedVariable
    ar = Arrows.objects.order_by('-pk')[:4]  # @UndefinedVariable
    ac = Accessories.objects.order_by('-pk')[:4]  # @UndefinedVariable
    
    d = rec_result(request.user.id)
    
    try:
        try:
            bow = Bows.objects.filter(id__in=d['bow'])  # @UndefinedVariable
         
        except Bows.DoesNotExist:
            bow = None
    except KeyError:
        bow = None
    
    try:
        try:
            arrow = Arrows.objects.filter(id__in=d['arrow'])  # @UndefinedVariable
         
        except Arrows.DoesNotExist:
            arrow = None
    except KeyError:
        arrow = None

    try:
        try:
            accessory = Accessories.objects.filter(id__in=d['accessory'])  # @UndefinedVariable
         
        except Accessories.DoesNotExist:
            accessory = None
    except KeyError:
        accessory = None

    
    return render_to_response('index.html', RequestContext(request, {'user':request.user,'arrow_rec':arrow,'accessory_rec':accessory,'bow_rec':bow,'bows':b,'arrows':ar,'accessories':ac}))

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


