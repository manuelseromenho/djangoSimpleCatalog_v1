#django imports
from django.shortcuts import render
from django.core.mail import send_mail
import stripe

#local imports
from .models import OrderItem, Order
from .forms import OrderCreateForm, UserCreateForm,PerfilCreateForm
from cart.models import Carrinho, Item
from shop.models import Perfil
from myshop import settings

def order_create(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    #carrinho = Carrinho(request)
    utilizador = request.user
    perfil = Perfil.objects.filter(utilizador=utilizador).last()

    carrinho = Carrinho.objects.filter(utilizador=utilizador).last()
    itens_carrinho = Item.objects.filter(carrinho=carrinho)
    valor_total_pagamento = int(carrinho.total * 100)
    flag_required = 0


    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        # if not form.is_valid():
        #     flag_required = 1
        #     order = Order.objects.get(id=utilizador.id)
        #     return render(request,
        #                   'orders/order/create.html',
        #                   {'order': order,'flag_required': flag_required})
        # elif \
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
                send_mail('ENCOMENDA REALIZADA nr ' + str(nr_de_encomenda) + ' na RogueBit Shop',
                          'ENCOMENDA REALIZADA nr ' + str(nr_de_encomenda),
                          'geral@inforzen.pt',
                          ['manuelseromenho@gmail.com']) #[utilizador.email]



                # enviar email para empresa
                string_subject_empresa = 'ENCOMENDA REALIZADA nr ' + str(nr_de_encomenda) + ' na RogueBit Shop'

                string_email_empresa = 'ENCOMENDA REALIZADA nr ' \
                                       + str(nr_de_encomenda) + ' pelo/a cliente ' + utilizador.first_name + ' ' \
                                       + utilizador.last_name + ' com a morada de entrega: ' + perfil.endereco_envio \
                                       + ' e morada de faturação: ' +  perfil.endereco_faturacao
                send_mail(string_subject_empresa, string_email_empresa,'postmaster@sandbox5e65addc56f44613bc8755aa1da8e3d4.mailgun.org',
                          ['geral@inforzen.pt'])

                token = request.POST.get("stripeToken")

                try:
                    charge = stripe.Charge.create(
                        amount=valor_total_pagamento,
                        currency="eur",
                        source=token,
                        description=string_email_empresa
                    )
                except stripe.error.CardError as ce:
                    return False, ce

        # clear the cart
        carrinho.delete()


        user_form = UserCreateForm(
            instance=request.user,
            data=request.POST)
        perfil_form = PerfilCreateForm(
            instance=request.user.perfil,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()


        return render(request,'orders/order/created.html',
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
             'utilizador':utilizador,
             'pk_stripe': settings.STRIPE_PUBLIC_KEY,
             'valor_total_pagamento': valor_total_pagamento})