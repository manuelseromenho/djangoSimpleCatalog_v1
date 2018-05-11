#django imports
from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from collections import OrderedDict

#local imports
from .models import Perfil

class AdminPasswordChangeForm(forms.Form):

    new_password1 = forms.CharField(
        label=("Passe"),
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('new_password1')
        labels = {'new_password1':'nova passe'}


class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(label='Passe antiga',
                                   widget=forms.PasswordInput)

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Palavra-Passe',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Palavra-Passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name', 'email')
        labels = {'username':'utilizador', 'first_name':'primeiro nome'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    #password = forms.CharField(label='Palavra-Passe', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name','last_name','email')


class PerfilEditForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('endereco_envio','endereco_faturacao', 'nif','metodo_pagamento', 'data_nascimento', 'foto')

