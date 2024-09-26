import requests
from datetime import date, timedelta


def getData(day):
    today = date.today()
    dayToGetData = today + timedelta(days=day)
    url = f'https://epg.rsi.ch/mp-epg-frontend-api/web/la1?StartTime={dayToGetData}T00:00:00%2B02:00&EndTime={dayToGetData}T23:59:59%2B02:00'

    response = requests.get(url)
    if response.status_code == 200:  # Controlla che la richiesta sia andata a buon fine
        return response.json()  # Restituisci il JSON
    else:
        return {'error': 'Failed to retrieve data',
                'status_code': response.status_code}  # Restituisci un errore in caso di fallimento

def getPrograms(data):
    programs = []
    if 'program' in data:
        for program_data in data['program']:
            program = Program(program_data)
            programs.append(program)

    return programs

class Program:
    def __init__(self, data):
        self.title = data["content"]["title"]
        self.description = data["content"]["longDescription"]
        self.eppisodes = data["content"]["episodeNr"]
        self.people = data["people"]
        self.image = data["srgPlay"]["Image"]["ImageRepresentation"]["variants"]
        self.channel = data["channel"]
        self.productionYear = data["content"]["productionYear"]
        self.productTypeDesc = data["content"]["productTypeDesc"]
        self.kind = data["kind"]
        self.date = data["dateTimes"]["startTime"]
        self.duration = data["dateTimes"]["realDuration"]