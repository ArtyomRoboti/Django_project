from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
# Create your views here.
def main_page(request):

    return render(request, 'menu.html')

def games_page(request):
    games = Game.objects.all()
    # games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'games': games
    }
    return render(request, 'games.html', context)

def cart_page(request):
    return render(request, 'cart.html')

def sign_up_by_django(request):
    info = {}
    buyers = Buyer.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            balance = form.cleaned_data['balance']
            age = form.cleaned_data['age']
            info['form'] = form
        else:
            form = UserRegister()
            info['form'] = form
        for buyer in buyers:
            if buyer.name == name:
                return HttpResponse(f'Пользователь "{name}" уже зарегестрирован!')
        else:
            Buyer.objects.create(name=name, balance=balance, age=age)

    return render(request, 'registration_page.html', info)

def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and int(age) >= 18 and username not in users:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(info['error'])
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse(info['error'])
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse(info['error'])
    return render(request, 'registration_page.html', info)
