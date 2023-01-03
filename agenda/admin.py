from django.contrib import admin
from .models import Barbeiro, Serviço, Agendamento


admin.site.register(Barbeiro)
admin.site.register(Serviço)
admin.site.register(Agendamento)
