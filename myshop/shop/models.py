from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Categoria(models.Model):

    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class SubCategoria(models.Model):

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, db_index=True, null = True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'subcategoria'
        verbose_name_plural = 'subcategorias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('shop:product_list_by_subcategory', args=[self.slug])


class Produto(models.Model):

    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    descricao = models.TextField(max_length=300, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('shop:product_details', args=[self.slug])


class Perfil(models.Model):
    utilizador = models.OneToOneField(User)
    data_nascimento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='utilizadores/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Perfil do utilizador{}'.format(self.utilizador.username)