#django imports
from django.db import models

#local imports
from shop.models import Produto


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    endereco_envio = models.CharField(max_length=250)
    endereco_faturacao = models.CharField(max_length=250)
    metodo_pagamento = models.CharField(max_length=20, null=True)
    nif = models.CharField(max_length=11, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Encomenda nr: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    produto = models.ForeignKey(Produto,
        related_name='order_items')

    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.preco * self.quantidade
