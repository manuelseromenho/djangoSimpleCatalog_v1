#django imports
from django.shortcuts import render

#local imports
from .models import OrderItem, Order
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
            nr_de_encomenda = Order.objects.first()

            for item in itens_carrinho:
                OrderItem.objects.create(order=order,
                    produto=item.produto,
                    preco=item.get_total_price() , #preco total dos elementos da linha
                    quantidade=item.quantidade)

                # remover stock após venda
                item.produto.stock = item.produto.stock - item.quantidade
                item.produto.save()


                # enviar email para cliente
                from django.core.mail import send_mail
                send_mail('ENCOMENDA REALIZADA nr ' + str(nr_de_encomenda) + ' na RogueBit Shop',
                          'ENCOMENDA REALIZADA nr ' + str(nr_de_encomenda),
                          'geral@inforzen.pt',
                          ['manuelseromenho@gmail.com']) #[utilizador.email]



                # enviar email para empresa
                from django.core.mail import send_mail
                send_mail('ENCOMENDA REALIZADA nr ' + str(nr_de_encomenda) + ' na RogueBit Shop',
                          'ENCOMENDA REALIZADA nr ' + str(nr_de_encomenda) + ' pelo/a cliente ' + utilizador.first_name + ' ' + utilizador.last_name,
                          'postmaster@sandbox5e65addc56f44613bc8755aa1da8e3d4.mailgun.org',
                          ['geral@inforzen.pt'])

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