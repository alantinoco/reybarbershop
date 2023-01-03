from django.shortcuts import render

def index(request):
    return render(request, 'agendamento.html')


def tabelaDePrecos(request):
    return render(request, 'tabelaDePrecos.html')