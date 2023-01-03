from django.shortcuts import render

def index(request):
    return render(request, 'agendamento.html')


def tabelaDePrecos(request):
    return render(request, 'tabelaDePrecos.html')

def agendaRonaldo(request):
    return render(request, 'ronaldo.html')


def agendaVagner(request):
    return render(request, 'vagner.html')


def agendaGabriel(request):
    return render(request, 'gabriel.html')