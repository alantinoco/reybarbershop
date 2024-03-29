# Generated by Django 4.1.5 on 2023-01-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='barbeiro',
            field=models.CharField(choices=[('Ronaldo', 'Ronaldo'), ('Vagner', 'Vagner'), ('Gabriel', 'Gabriel')], max_length=20),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='horaAgendamento',
            field=models.CharField(choices=[('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00')], max_length=20),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='servico',
            field=models.CharField(blank=True, choices=[('corte', 'corte'), ('barba', 'barba'), ('corte + barba', 'corte + barba'), ('pezinho', 'pezinho')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Barbeiro',
        ),
        migrations.DeleteModel(
            name='Serviço',
        ),
    ]
