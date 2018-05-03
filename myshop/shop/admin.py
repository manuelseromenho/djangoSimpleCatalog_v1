from django.contrib import admin
from .models import Categoria, SubCategoria, Produto, Perfil, Carrinho, Item


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug':('nome',)}


admin.site.register(Categoria, CategoriaAdmin)


class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria', 'subcategoria', 'slug']
    prepopulated_fields = {'slug':('nome',)}

    # De maneira  poder personalizar o nome do campo na admin
    # e manter a ordenação através do "nome"
    def subcategoria(self, obj):
        return ("%s" % (obj.nome))
    subcategoria.short_description = "SubCategoria"
    subcategoria.admin_order_field = "nome"


admin.site.register(SubCategoria, SubCategoriaAdmin)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug", "preco", "stock", "disponivel", "criado", "atualizado"]
    list_filter = ["disponivel", "criado", "atualizado"]
    list_editable = ['preco', 'stock', 'disponivel']
    prepopulated_fields = {'slug':('nome',)}


admin.site.register(Produto, ProdutoAdmin)


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['utilizador', 'data_nascimento', 'foto']

admin.site.register(Perfil, PerfilAdmin)


class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ["utilizador", "total", "criado", "atualizado"]
    list_filter = ["criado"]
    list_editable = ["utilizador"]

admin.site.register(Carrinho, CarrinhoAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ["item", "carrinho", "quantidade"]
    list_filter = ["carrinho"]
    list_editable = ["item", "carrinho", "quantidade"]

admin.site.register(Item, ItemAdmin)