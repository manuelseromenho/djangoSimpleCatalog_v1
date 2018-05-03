from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Categoria, SubCategoria, Produto, Perfil, Carrinho, Item
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, PerfilEditForm



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

    #if request.method == 'GET':
    produto = get_object_or_404(Produto, slug=product_slug)

    return render(request,'shop/produto/details.html',
    {'produto': produto})



def adicionar_carrinho(request):
    slug = request.POST.get('slug', '')
    if request.method == 'POST':
        produto = get_object_or_404(Produto, slug=slug)

        #Pesquisar por utilizador
        utilizador = request.user

        #Filtrar carrinho por user, se não existir criar
        carrinho = Carrinho.objects.filter(utilizador=utilizador).first()

        #Com o carrinho verificar se existem o item dentro do carrinho
        # se existir aumenta a quantidade
        # cc Cria o item e adiciona ao carrinho

        #return render(request, 'shop/cart.html', {'produto': produto})


def mostrar_carrinho(request):

    #if request.method == 'POST':
        utilizador = request.user
        #Filtrar carrinho por user, se não existir criar
        carrinho = Carrinho.objects.filter(utilizador=utilizador).first()
        itens = Item.objects.filter(carrinho = carrinho)

        #Com o carrinho verificar se existem o item dentro do carrinho
        # se existir aumenta a quantidade
        # cc Cria o item e adiciona ao carrinho
        return render(request, 'shop/cart.html', {'itens': itens})




@login_required
def dashboard(request):
    profile_foto = None

    # I'm almost certain that this check becomes redundant with the above decorator
    if request.user.is_authenticated:
        try:
            profile = Perfil.objects.get(utilizador=request.user)
            profile_foto = profile.foto
        except ObjectDoesNotExist:
            pass

    return render(request,'shop/dashboard.html',{
        'section': 'dashboard',
        'foto': profile_foto
    })


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
            # Create the user profile
            perfil = Perfil.objects.create(utilizador=new_user)
            return render(request,
                          'register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST)
        perfil_form = PerfilEditForm(
            instance=request.user.perfil,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilEditForm(instance=request.user.perfil)
    return render(request,'shop/edit.html',{'user_form': user_form,'perfil_form': perfil_form})

