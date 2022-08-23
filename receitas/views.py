from django.shortcuts import render


def home(request):
    return render(request, 'receitas/home.html')


def contato(request):
    return render(request, 'receitas/contato.html')


def sobre(request):
    return render(request, 'receitas/sobre.html')
