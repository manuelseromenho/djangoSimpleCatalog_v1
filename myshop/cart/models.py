#django imports
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.urlresolvers import reverse

#local imports
from shop.models import Produto


class Carrinho(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def get_total_items(self):
        total = 0
        return total

    def __str__(self):
        return str(self.id)

    def valor_total_carrinho(self):
        result = sum(itens.produto.preco * itens.quantidade for itens in self.item_set.all())
        self.total = result


class Item(models.Model):

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, null=True)
    quantidade = models.PositiveIntegerField()

    # para garantir que o item não se repete no mesmo carrinho
    class Meta:
        unique_together = ('produto', 'carrinho')

    def __str__(self):
        return self.produto.nome

    def get_total_price(self):
        return self.produto.preco * self.quantidade



#Possiveis Signals

# @receiver(post_save, sender=Item, dispatch_uid="update_total_cart")
# def update_total(sender, instance, **kwargs):
#     instance.carrinho.valor_total_carrinho()
#
#     post_save.disconnect(sender=Item)
#     instance.carrinho.save()
#     post_save.connect(update_total, sender=Item)


# @receiver(post_delete, sender=Item, dispatch_uid="update_total_cart_delete")
# def update_total_delete(sender, instance, **kwargs):
#
#     carrinho = instance.carrinho
#     itens = Item.objects.filter(carrinho=carrinho)
#     total = sum(i.produto.preco * i.quantidade for i in itens)
#     instance.carrinho.total = total
#
#     post_delete.disconnect(sender=Item)
#     instance.carrinho.save()
#     post_delete.connect(update_total_delete, sender=Item)
