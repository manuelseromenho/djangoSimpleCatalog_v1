from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import SubCategoria, Produto


# # def index(request):
#     return HttpResponse('Awesome')


def product_list(request, sub_category_slug=None):

    subcategoria = None
    subcategorias = SubCategoria.objects.all()
    produtos = Produto.objects.filter(disponivel=True)

    if sub_category_slug:
        subcategoria = get_object_or_404(SubCategoria, slug=sub_category_slug)
        produtos = produtos.filter(subcategoria=subcategoria)

    return render(request,'shop/produto/list.html',
        {'subcategoria': subcategoria,
         'subcategorias': subcategorias,
         'produtos': produtos})
