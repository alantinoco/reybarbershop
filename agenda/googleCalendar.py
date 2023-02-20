from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleCalendar:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    FILE_PATH = 'secret_key.json'

    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            filename=self.FILE_PATH, scopes=self.SCOPES
        )
        self.service = build('calendar', 'v3', credentials=credentials)

    def add_event(self, nomeCliente, telCliente, barbeiro, servico, dataAgendamentoToCalendar, horaAgendamento):

        ronaldo = "85b08ccb13cb7c316921c380a39f5e674a16c03964c1040218920def9edcb285@group.calendar.google.com"
        vagner = "63020750722e60df84491918be7ce325aa0d7b915da68af28d8ac3ebf9b7118b@group.calendar.google.com"
        gabriel = "b74e45caec7ca87af3c27e1c91913a9ae69e44642e62401bdb53b7ba36d162b4@group.calendar.google.com"
        calendar_id= ""
                
        fimDoAtendimento = horaAgendamento[0:3:1]+'30'
        

        event = {
                'summary': nomeCliente +" - "+telCliente,
                'location': barbeiro,
                'description': servico,
                'start': {
                    'dateTime': dataAgendamentoToCalendar+'T'+horaAgendamento+':00',
                    'timeZone': 'America/Sao_Paulo',
                },
                'end': {
                    'dateTime': dataAgendamentoToCalendar+'T'+fimDoAtendimento+':00',
                    'timeZone': 'America/Sao_Paulo',
                },
            }
        
        if event.get('location') == "Ronaldo":
            calendar_id = ronaldo
            event = self.service.events().insert(calendarId=calendar_id, body=event).execute()
        elif event.get('location') == "Vagner":
            calendar_id = vagner
            event = self.service.events().insert(calendarId=calendar_id, body=event).execute()
        else:
            event = self.service.events().insert(calendarId=gabriel, body=event).execute()
            



calendar = GoogleCalendar()



# To get an event
# myEvent = calendar.service.events().get(calendarId='732ef43aa77457cce14ebab35ad9a7caa9b49d3880c08e7db7a48a716a5dc9f6@group.calendar.google.com', eventId='6afq4uf1h0lq7um7oo84nv9ais').execute()
# print(myEvent['summary']+'\n'+myEvent['description'])

# To delete an event
# calendar.service.events().delete(calendarId='primary', eventId='eventId').execute()

