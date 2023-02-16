from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("consulta/agendamento", views.consultaAgendamento, name="consultaAgendamento"),
    path("precos", views.tabelaDePrecos, name="precos"),
    path("agenda/ronaldo", views.agendaRonaldo, name="ronaldo"),
    path("agenda/vagner", views.agendaVagner, name="vagner"),
    path("agenda/gabriel", views.agendaGabriel, name="gabriel"),
]