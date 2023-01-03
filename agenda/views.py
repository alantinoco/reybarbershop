from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from .models import Agendamento

def index(request):
    form = AgendamentoForm()

    context = {
        'form': form,
    }

    if request.method == "POST":
        form = AgendamentoForm(request.POST or None)
        if form.is_valid():
            nomeCliente = form.cleaned_data.get('nomeCliente')
            telCliente = form.cleaned_data.get('telCliente')
            barbeiro = form.cleaned_data.get('barbeiro')
            dataAgendamento = form.cleaned_data.get('dataAgendamento')
            servico = form.cleaned_data.get('servico')
            horaAgendamento = form.cleaned_data.get('horaAgendamento')
            Agendamento.objects.create(
                    nomeCliente = nomeCliente, 
                    telCliente = telCliente,
                    barbeiro = barbeiro,
                    dataAgendamento = dataAgendamento,
                    servico = servico,
                    horaAgendamento = horaAgendamento
                )
            return redirect('index')
    return render(request, 'agendamento.html')


def tabelaDePrecos(request):
    return render(request, 'tabelaDePrecos.html')

def agendaRonaldo(request):
    return render(request, 'ronaldo.html')


def agendaVagner(request):
    return render(request, 'vagner.html')


def agendaGabriel(request):
    return render(request, 'gabriel.html')