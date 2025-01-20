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


users = ['user1', 'user2', 'user3']


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка условий
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            # Успешная регистрация
            return render(request, 'success.html', {'message': f'Приветствуем, {username}!'})

    return render(request, 'registration_page.html', {'info': info})


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка условий
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            # Успешная регистрация
            return render(request, 'success.html', {'message': f'Приветствуем, {username}!'})

    return render(request, 'registration_page.html', {'info': info})
