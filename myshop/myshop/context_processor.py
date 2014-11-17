from shopcart.models import Cart

def data(request):
    try:
        a = Cart.objects.get(user_id1=request.user.id)
        a = eval(a.data)
    except Cart.DoesNotExist:
        a = None
    return {'data':a}