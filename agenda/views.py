from django.shortcuts import render, redirect
from .forms import AgendamentoForm, ConsultaAgendamentoForm, CancelaAgendamentoForm
from .models import Agendamento
from .googleCalendar import calendar
from django.contrib import messages


def index(request):
    form = AgendamentoForm()

    if request.method == "POST":
        form = AgendamentoForm(request.POST or None)
        if form.is_valid():
            nomeCliente = form.cleaned_data.get('nomeCliente')
            telCliente = form.cleaned_data.get('telCliente')
            barbeiro = form.cleaned_data.get('barbeiro')
            dataAgendamento = form.cleaned_data.get('dataAgendamento')
            servico = form.cleaned_data.get('servico')
            horaAgendamento = form.cleaned_data.get('horaAgendamento')
            
            agendamentoExiste = Agendamento.objects.filter(telCliente=telCliente, dataAgendamento=dataAgendamento, horaAgendamento=horaAgendamento)
            print(agendamentoExiste)

            if agendamentoExiste:
                messages.error(request, ("Data/Hora já ocupada! Favor checar disponibilidade em Agenda Dos Barbeiros."))
                return redirect('index')
            else:
                Agendamento.objects.create(
                    nomeCliente = nomeCliente, 
                    telCliente = telCliente,
                    barbeiro = barbeiro,
                    dataAgendamento = dataAgendamento,
                    servico = servico,
                    horaAgendamento = horaAgendamento
                )
                dataAgendamentoToCalendar = str(dataAgendamento)
                calendar.add_event(nomeCliente, telCliente, barbeiro, servico, dataAgendamentoToCalendar, horaAgendamento)
                return redirect('index')
    return render(request, 'agendamento.html')


def visualizarAgendamento(request, id):
    agendamento = Agendamento.objects.filter(id=id)
    return render(request, 'consultaAgendamento.html', {'agendamento' : agendamento})

def consultaAgendamento(request):
    form = ConsultaAgendamentoForm()
    if request.method == "POST":
        form = ConsultaAgendamentoForm(request.POST or None)
        if form.is_valid():
            telCliente = form.cleaned_data.get('telCliente')
            dataAgendamento = form.cleaned_data.get('dataAgendamento')
            agendamentoBuscado = Agendamento.objects.filter(dataAgendamento=dataAgendamento,telCliente=telCliente)
            if agendamentoBuscado:
                return render(request, 'visualizarAgendamento.html', {'agendamentoBuscado': agendamentoBuscado})
            else:
                messages.error(request, ("Nenhum agendamento encontrado"))
    return render(request, 'consultaAgendamento.html')

def cancelaAgendamento(request):
    form = CancelaAgendamentoForm()
    if request.method == "POST":
        form = CancelaAgendamentoForm(request.POST or None)
        if form.is_valid():
            print(form.is_valid())
            telCliente = form.cleaned_data.get('telCliente')
            barbeiro = form.cleaned_data.get('barbeiro')
            dataAgendamento = form.cleaned_data.get('dataAgendamento')
            dataAgendamentoToCalendar = str(dataAgendamento)
            calendar.del_event(telCliente, barbeiro ,dataAgendamentoToCalendar)

            print(telCliente)
            print(barbeiro)
            print(dataAgendamento)
            print(dataAgendamentoToCalendar)

            agendamentoParaCancelar = Agendamento.objects.filter(
                dataAgendamento=dataAgendamento,
                telCliente=telCliente, 
                barbeiro=barbeiro
            )
            agendamentoParaCancelar.delete()
            return redirect('index')
    return render(request, 'cancelaAgendamento.html')


    
    return render(request, 'tabelaDePrecos.html')

def tabelaDePrecos(request):
    return render(request, 'tabelaDePrecos.html')

def agendaRonaldo(request):
    return render(request, 'ronaldo.html')


def agendaVagner(request):
    return render(request, 'vagner.html')


def agendaGabriel(request):
    return render(request, 'gabriel.html')