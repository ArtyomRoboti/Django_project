from django import forms

class UserRegister(forms.Form):
    name = forms.CharField(max_length=30, label='Введите имя:')
    balance = forms.CharField(max_length=8, label='Введите баланс:')
    age = forms.CharField(max_length=3, label='Введите свой возраст:')