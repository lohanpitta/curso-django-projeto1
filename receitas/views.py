from django.shortcuts import render
from util.receitas.factory import make_recipe


def home(request):
    return render(request, 'receitas/paginas/home.html', context={
        'receitas': [make_recipe() for _ in range(10)],
    })


def receitas(request, id):
    return render(request, 'receitas/paginas/receitas-view.html')
