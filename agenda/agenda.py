from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta

scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file("../client_secret.json", scopes=scopes)

#credentials = flow.run_console()
#pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("../token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

ronaldo = "d44f9e84cc34f69078879f234668307cc4fc2bd665ab4fc2b91e898097b2f539@group.calendar.google.com"
vagner = "66993382a4a839d6735728b3ec8b5631b70cfcc147a42dffa6d7bf9fd031b246@group.calendar.google.com"
gabriel = "0437240bd92cd330d05b3a21b37d68c73f86ee49f31791f7db186d29fbc5743b@group.calendar.google.com"

# List all events
events = service.events().list(calendarId = ronaldo, timeZone = "America/Sao_Paulo").execute()

print(events)