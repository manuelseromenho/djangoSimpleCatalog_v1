from django.contrib.auth.models import User
from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse

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


class Item(models.Model):

    item = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, null=True)
    quantidade = models.PositiveIntegerField()

    # para garantir que o item não se repete no mesmo carrinho
    class Meta:
        unique_together = ('item', 'carrinho')

    def __str__(self):
        return str(self.item.nome)




