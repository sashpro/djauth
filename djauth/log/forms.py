# -*- encoding: utf-8
#from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegForm(UserCreationForm):
    #name = forms.CharField(label='Логин', max_length=20)
    #password = forms.CharField(label='Пароль', max_length=20, widget=forms.PasswordInput())
    pass
    class Meta:
        model = User
        fields = ("username", "sex")