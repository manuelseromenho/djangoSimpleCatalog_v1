from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Categoria, SubCategoria, Produto


# # def index(request):
#     return HttpResponse('Awesome')


def product_list(request, sub_category_slug=None, category_slug=None):

    categoria = None
    categorias = Categoria.objects.all()

    subcategoria = None
    subcategorias = SubCategoria.objects.all()

    produtos = Produto.objects.filter(disponivel=True)

    if category_slug:
        categoria = get_object_or_404(Categoria, slug=category_slug)
        produtos = produtos.filter(categoria=categoria)


    if sub_category_slug:
        subcategoria = get_object_or_404(SubCategoria, slug=sub_category_slug)
        produtos = produtos.filter(subcategoria=subcategoria)

    return render(request,'shop/produto/list.html',
        {
            # 'categoria': categoria,
            # 'categorias': categorias,
            'subcategoria': subcategoria,
            'subcategorias': subcategorias,
            'produtos': produtos
        })


def product_details(request, product_slug):

    # produto = Produto.objects.filter(slug=product_slug).first()
    # produto = Produto.objects.get(slug=product_slug)
    produto = get_object_or_404(Produto, slug=product_slug)



    return render(request,'shop/produto/details.html',
        {'produto': produto,})
