from django import forms
from .models import Order
from cart.models import Carrinho, Item
from shop.models import Perfil
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email']


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')


class PerfilCreateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('endereco_envio','endereco_faturacao', 'nif','metodo_pagamento')
