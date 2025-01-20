from django.shortcuts import render

from task5.forms import UserRegister


# Create your views here.
def platform_page(request):
    return render(request, 'fourth_task/platform.html')


def games_page(request):
    return render(request, 'fourth_task/games.html')


def cart_page(request):
    context = {
        'games': ["Atomic Heart", "Cyberpunk 2077", "Айболит"]}
    return render(request, 'fourth_task/cart.html', context)

