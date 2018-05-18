from django import forms
from .models import Order
from cart.models import Carrinho, Item
from shop.models import Perfil
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'endereco_envio','endereco_faturacao', 'nif','metodo_pagamento']


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')


class PerfilCreateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('endereco_envio','endereco_faturacao', 'nif','metodo_pagamento')

    def __init__(self, *args, **kwargs):
        super(PerfilCreateForm, self).__init__(*args, **kwargs)

        # for key in self.fields:
        self.fields['endereco_envio'].required = True
        self.fields['endereco_faturacao'].required = True

