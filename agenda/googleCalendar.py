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
            

    def del_event(self, telCliente, barbeiro, dataAgendamentoToCalendar):

        ronaldo = "85b08ccb13cb7c316921c380a39f5e674a16c03964c1040218920def9edcb285@group.calendar.google.com"
        vagner = "63020750722e60df84491918be7ce325aa0d7b915da68af28d8ac3ebf9b7118b@group.calendar.google.com"
        gabriel = "b74e45caec7ca87af3c27e1c91913a9ae69e44642e62401bdb53b7ba36d162b4@group.calendar.google.com"

        if barbeiro == "Ronaldo":
            events = calendar.service.events().list(calendarId=ronaldo).execute()
            for event in events['items']:
                if telCliente in event['summary'] and dataAgendamentoToCalendar in event['start']['dateTime']:
                    calendar.service.events().delete(calendarId=ronaldo, eventId = event['id']).execute()
        elif barbeiro == "Vagner":
                events = calendar.service.events().list(calendarId=vagner).execute()
                for event in events['items']:
                    if telCliente in event['summary'] and dataAgendamentoToCalendar in event['start']['dateTime']:
                        calendar.service.events().delete(calendarId=ronaldo, eventId = event['id']).execute()
        else:
            events = calendar.service.events().list(calendarId=gabriel).execute()
            for event in events['items']:
                if telCliente in event['summary'] and dataAgendamentoToCalendar in event['start']['dateTime']:
                    calendar.service.events().delete(calendarId=gabriel, eventId = event['id']).execute()


calendar = GoogleCalendar()





# for event in events['items']:
#     if "1111111111" in event['summary'] and '2023-03-18' in event['start']['dateTime']:
#         print(event['summary'])
#         print(event['start']['dateTime'])
#         calendar.service.events().delete(calendarId = "85b08ccb13cb7c316921c380a39f5e674a16c03964c1040218920def9edcb285@group.calendar.google.com", eventId = event['id']).execute()
#         print("Evento deletado")
#     else:
#         print("Nenhum evento encontrado")
#         break
        


        # horaAgendamento = event['start']
        # for item in horaAgendamento.values():
        #     print(item)





{'kind': 'calendar#event', 
 'etag': '"3358106545324000"', 
 'id': 'sva9glh9jromcp66c17go298cs', 
 'status': 'confirmed', 
 'htmlLink': 'https://www.google.com/calendar/event?eid=c3ZhOWdsaDlqcm9tY3A2NmMxN2dvMjk4Y3MgODViMDhjY2IxM2NiN2MzMTY5MjFjMzgwYTM5ZjVlNjc0YTE2YzAzOTY0YzEwNDAyMTg5MjBkZWY5ZWRjYjI4NUBn', 
 'created': '2023-03-17T11:41:12.000Z', 
 'updated': '2023-03-17T11:41:12.662Z', 
 'summary': 'Jon - 11111111111', 
 'description': 'corte + barba', 
 'location': 'Ronaldo', 
 'creator': {'email': 'conta-de-servico-reybarbershop@reybarbershop113.iam.gserviceaccount.com'}, 
 'organizer': {'email': '85b08ccb13cb7c316921c380a39f5e674a16c03964c1040218920def9edcb285@group.calendar.google.com', 
               'displayName': 'Ronaldo', 'self': True}, 
 'start': {'dateTime': '2023-03-18T10:00:00-03:00', 'timeZone': 'America/Sao_Paulo'}, 
 'end': {'dateTime': '2023-03-18T10:30:00-03:00', 'timeZone': 'America/Sao_Paulo'}, 
 'iCalUID': 'sva9glh9jromcp66c17go298cs@google.com', 
 'sequence': 0, 
 'reminders': {'useDefault': True}, 
 'eventType': 'default'
}






# To get an event
# myEvent = calendar.service.events().get(calendarId='732ef43aa77457cce14ebab35ad9a7caa9b49d3880c08e7db7a48a716a5dc9f6@group.calendar.google.com', eventId='6afq4uf1h0lq7um7oo84nv9ais').execute()
# print(myEvent['summary']+'\n'+myEvent['description'])

# To delete an event
# calendar.service.events().delete(calendarId='primary', eventId='eventId').execute()

