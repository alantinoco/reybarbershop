from django.db import models

class Barbeiro(models.Model):
    nomeBarbeiro = models.CharField(max_length=50)
    telBarbeiro = models.CharField(max_length=11)
    estaAtivo = models.BooleanField()

    def __str__(self):
        return self.nomeBarbeiro

class Serviço(models.Model):
    nomeServico = models.CharField(max_length=30)
    precoServico = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.serviceName) + ": $" + str(self.servicePrice)


class Agendamento(models.Model):
    nomeCliente = models.CharField(max_length=50)
    telCliente = models.CharField(max_length=11)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    servico = models.ForeignKey(Serviço, null=True, blank=True, on_delete=models.CASCADE)
    dataAgendamento = models.DateField()
    horaAgendamento = models.CharField(max_length=20)
    compareceu = models.BooleanField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True, max_length=240)

    def __str__(self):
        return self.clientName + '' + self.barber + '' + self.date
