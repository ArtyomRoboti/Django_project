from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'platform.html')

def games_page(request):
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay 2'
    context = {
        'game1': game1,
        'game2': game2,
        'game3': game3
    }
    return render(request, 'games.html', context)

def cart_page(request):
    return render(request, 'cart.html')