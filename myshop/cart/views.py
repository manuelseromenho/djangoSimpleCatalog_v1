#global imports
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import DeleteView


#local imports
from shop.models import Produto
from .models import Carrinho, Item


# class ItemDelete(DeleteView):
#     model = Item
#     success_url = '/carrinho'
    #pk_url_kwarg = "id"

def delete_item(request, pk):
    try:

        item = Item.objects.get(id=pk)
        item.delete()

        utilizador = request.user
        carrinho = Carrinho.objects.filter(utilizador=utilizador).last()
        itens = Item.objects.filter(carrinho=carrinho)
        total = sum(i.produto.preco * i.quantidade for i in itens)
        carrinho.total = total
        carrinho.save()

    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse("cart:mostrar_carrinho"))
    return HttpResponseRedirect(reverse("cart:mostrar_carrinho"))


def delete_all_items(request):
    try:

        item = Item.objects.all()
        item.delete()

        utilizador = request.user
        carrinho = Carrinho.objects.filter(utilizador=utilizador).last()
        itens = Item.objects.filter(carrinho=carrinho)
        total = sum(i.produto.preco * i.quantidade for i in itens)
        carrinho.total = total
        carrinho.save()

    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse("cart:mostrar_carrinho"))
    return HttpResponseRedirect(reverse("cart:mostrar_carrinho"))


def adicionar_carrinho(request):
    slug = request.POST.get('slug', '')
    quantity = request.POST.get("quantity", "")

    if request.method == 'POST':
        produto = get_object_or_404(Produto, slug=slug)

        if quantity == '':
            return render(request, 'shop/produto/details.html', {'produto': produto, 'erro_stock': 1})
        elif int(quantity) < 1 or produto.stock<int(quantity):
            return render(request, 'shop/produto/details.html', {'produto': produto, 'erro_stock': 1})

        # Pesquisar por utilizador
        utilizador = request.user

        # ***** Filtrar carrinho por user, se não existir criar
        if Carrinho.objects.filter(utilizador=utilizador):
            carrinho = Carrinho.objects.filter(utilizador=utilizador).last()
        else:
            carrinho = Carrinho(utilizador= utilizador)
            carrinho.save()


        # Com o carrinho verificar se existem o item dentro do carrinho
        # se existir aumenta a quantidade
        # cc Cria o item e adiciona ao carrinho
        item_repetido = Item.objects.filter(carrinho=carrinho, produto=produto).first()
        if not item_repetido:
            # Criar novo Item
            item = Item(
                produto=produto,
                quantidade=quantity,
                carrinho=carrinho
            )
            item.save()
        else:
            # Update Item
            item_repetido.quantidade += int(quantity)
            item_repetido.save()
            # return render(request, 'cart/cart.html')



        itens = Item.objects.filter(carrinho=carrinho)
        total = sum(i.produto.preco * i.quantidade for i in itens)
        carrinho.total = total
        carrinho.save()

        return mostrar_carrinho(request)






        # return render(request, 'cart/cart.html', {'produto': produto})


def mostrar_carrinho(request):

    utilizador = request.user

    # ***** Filtrar carrinho por user, se não existir criar
    if Carrinho.objects.filter(utilizador=utilizador):
        carrinho = Carrinho.objects.filter(utilizador=utilizador).last()
    else:
        carrinho = Carrinho(utilizador=utilizador)
        carrinho.save()

    #itens = Item.objects.filter(carrinho = carrinho).select_related('produto')
    itens = Item.objects.filter(carrinho=carrinho)

    # total = sum(i.produto.preco*i.quantidade for i in itens)
    total = carrinho.total

    #item = Item.objects.filter(item=id_produto).first()

    return render(request, 'cart/cart.html', {'itens': itens, 'total': total, })


def atualizar_carrinho(request):
    slug = request.POST.get('slug', '')
    quantity = request.POST.get("quantity", "")
    # slug = request.GET.get('slug')
    # quantity = request.GET.get("quantity")
    erro_stock = 0


    if request.method == 'POST':
        produto = get_object_or_404(Produto, slug=slug)

        # Pesquisar por utilizador
        utilizador = request.user

        # ***** Filtrar carrinho por user, se não existir criar
        if Carrinho.objects.filter(utilizador=utilizador):
            carrinho = Carrinho.objects.filter(utilizador=utilizador).last()
        else:
            carrinho = Carrinho(utilizador= utilizador)
            carrinho.save()

        itens = Item.objects.filter(carrinho=carrinho)
        item_repetido = Item.objects.filter(carrinho=carrinho, produto=produto).first()

        # Update Item
        if produto.stock >= int(quantity) and int(quantity)>0:
            item_repetido.quantidade = int(quantity)
            item_repetido.save()


            total = sum(i.produto.preco * i.quantidade for i in itens)
            carrinho.total = total
            carrinho.save()

            erro_stock = 0

            # answer = ""
            # data = {
            #     'respond': answer,
            #     'quantity': quantity,
            # }
            # return JsonResponse(data)
        else:
            erro_stock = 1
            total = carrinho.total
            # answer = "Valor Superior ao Stock Existente"
            # data = {
            #     'respond': answer,
            #     'quantity': quantity,
            # }
            # return JsonResponse(data)


    return render(request, 'cart/cart.html', {'itens': itens, 'total': total, 'erro_stock': erro_stock })


