from django import forms

class AgendamentoForm(forms.Form):

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

    nomeCliente = forms.CharField(max_length=50)
    telCliente = forms.CharField(max_length=11)
    barbeiro = forms.ChoiceField(choices=BARBEIROS)
    dataAgendamento = forms.DateField()
    servico = forms.ChoiceField(choices=SERVICO)
    horaAgendamento = forms.ChoiceField(choices=HORARIO)
    compareceu = forms.BooleanField(required=False)
    observacoes = forms.Textarea()



class ConsultaAgendamentoForm(forms.Form):
    telCliente = forms.CharField(max_length=11)
    dataAgendamento = forms.DateField()