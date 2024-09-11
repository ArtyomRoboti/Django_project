from django.shortcuts import render

# Create your views here.
def main_page(request):

    return render(request, 'menu.html')

def games_page(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'games': games
    }
    return render(request, 'games.html', context)

def cart_page(request):
    return render(request, 'cart.html')