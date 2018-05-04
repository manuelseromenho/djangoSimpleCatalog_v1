from django.contrib import admin
from .models import Carrinho, Item




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