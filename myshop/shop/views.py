from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Categoria, SubCategoria, Produto
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm



# # def index(request):
#     return HttpResponse('Awesome')


def product_list(request, sub_category_slug=None, category_slug=None):

    categoria = None
    categorias = Categoria.objects.all()

    subcategoria = None
    subcategorias = SubCategoria.objects.all()

    produtos = Produto.objects.filter(disponivel=True)

    preco_min = request.GET.get('preco_min', 0)
    preco_max = request.GET.get('preco_max', 10000)

    if not preco_min:
        preco_min = 0
    if not preco_max:
        preco_max = 3000

    produtos = produtos.filter(preco__gte=preco_min, preco__lte=preco_max)

    # if category_slug:
    #     categoria = get_object_or_404(Categoria, slug=category_slug)
    #     produtos = produtos.filter(categoria=categoria)


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

@login_required
def dashboard(request):
    return render(request,'shop/dashboard.html',{'section': 'dashboard'})


def register(request):
    if request.method == 'POST':

        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})