#django imports
from django.shortcuts import render

#local imports
from .models import OrderItem
from .forms import OrderCreateForm, UserCreateForm,PerfilCreateForm
from cart.models import Carrinho, Item
from shop.models import Perfil


def order_create(request):

    #carrinho = Carrinho(request)
    utilizador = request.user

    carrinho = Carrinho.objects.filter(utilizador=utilizador).last()
    itens_carrinho = Item.objects.filter(carrinho=carrinho)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in itens_carrinho:
                OrderItem.objects.create(order=order,
                    produto=item.produto,
                    preco=item.get_total_price() , #preco total dos elementos da linha
                    quantidade=item.quantidade)

                # remover stock após venda
                item.produto.stock = item.produto.stock - item.quantidade
                item.produto.save()

        # clear the cart


        carrinho.delete()

        return render(request,
            'orders/order/created.html',
            {'order': order})
    else:
        form = OrderCreateForm()
        utilizador_form = UserCreateForm(instance=request.user)

        perfil_form = PerfilCreateForm(instance=request.user.perfil)

    return render(request,
        'orders/order/create.html',
        {'itens_carrinho': itens_carrinho,
         'form': form,
         'utilizador_form': utilizador_form,
         'perfil_form': perfil_form,
         'carrinho':carrinho,
         'utilizador':utilizador })