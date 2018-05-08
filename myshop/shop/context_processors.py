#django imports
from django.contrib.auth.decorators import login_required
from django.contrib import auth

#local imports
from cart.models import Carrinho, Item


def total_on_base(request):

    utilizador = request.user
    if not utilizador.is_anonymous():
        carrinho = Carrinho.objects.filter(utilizador=utilizador).last()
        total_on_base = carrinho.total
    else:
        total_on_base = 0

    return {'total_on_base': total_on_base}