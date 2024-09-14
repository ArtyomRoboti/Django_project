from django.shortcuts import render
from numpy.ma.core import repeat
from django.http import HttpResponse
from .forms import UserRegister


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info['form'] = form
        else:
            form = UserRegister()
            info['form'] = form
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

