from django.shortcuts import render


# Create your views here.
def platform_page(request):
    return render(request, 'third_task/platform.html')


def games_page(request):
    return render(request, 'third_task/games.html')


def cart_page(request):
    context = {
        'items': {
            'Чебурашка': 'Непонятный зверь с большими ушами',
            'Чиполлино': 'Непонятный фрукт с большой головой',
            'Айболит': 'Понятный ветеринар с чемоданом',
        }
    }
    return render(request, 'third_task/cart.html', context)

# class ClassViews(TemplateView):
#     template_name = 'second_task/class_template.html'
