from django.db import models

class Agendamento(models.Model):

    BARBEIROS = (
                ('Ronaldo', 'Ronaldo'),
                ('Vagner', 'Vagner'),
                ('Gabriel', 'Gabriel')
            )

    SERVICO = (
                ('corte', 'corte'),
                ('barba', 'barba'),
                ('corte + barba', 'corte + barba'),
                ('pezinho', 'pezinho')
            )

    
    HORARIO = (
                ('10:00', '10:00'),
                ('11:00', '11:00'),
                ('12:00', '12:00'),
                ('13:00', '13:00'),
                ('14:00', '14:00'),
                ('15:00', '15:00'),
                ('16:00', '16:00'),
                ('17:00', '17:00'),
                ('18:00', '18:00'),
                ('19:00', '19:00'),
                ('20:00', '20:00'),
            )

    nomeCliente = models.CharField(max_length=50)
    telCliente = models.CharField(max_length=11)
    barbeiro = models.CharField(max_length=20, choices=BARBEIROS, blank=False, null=False)
    dataAgendamento = models.DateField()
    servico = models.CharField(max_length=20, choices=SERVICO, blank=True, null=True)
    horaAgendamento = models.CharField(max_length=20, choices=HORARIO, blank=False, null=False)
    compareceu = models.BooleanField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True, max_length=240)

    def __str__(self):
        return 'Agendamento confirmado para '+ str(self.dataAgendamento)[8:10]+'/'+str(self.dataAgendamento)[5:7] + ' as ' + str(self.horaAgendamento) + ' com o barbeiro ' + self.barbeiro
