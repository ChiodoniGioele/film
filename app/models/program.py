import requests
from datetime import date, timedelta



def getData(day,channel):
    today = date.today()
    dayToGetData = today + timedelta(days=day)
    url = f'https://epg.rsi.ch/mp-epg-frontend-api/web/{channel}?StartTime={dayToGetData}T00:00:00%2B02:00&EndTime={dayToGetData}T23:59:59%2B02:00'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to retrieve data',
                'status_code': response.status_code}

def getPrograms(data):
    programs = []
    if 'program' in data:
        for program_data in data['program']:
            program = Program(program_data)
            programs.append(program)
    return programs

class Program:
    def __init__(self, data):
        t = data["content"]["title"].split(" - ")
        self.title = t[0]
        self.subtitle = t[1] if len(t) > 1 else "-"
        self.description = data["content"].get("longDescription", "")
        self.episodes = data["content"].get("episodeNr", 0)
        self.people = data.get("people", [])
        self.image = data["srgPlay"]["Image"]["ImageRepresentation"][0]["variants"]
        self.channel = data.get("channel", "")
        self.productionYear = data["content"].get("productionYear", None)
        self.productTypeDesc = data["content"].get("productTypeDesc", "")
        self.kind = data.get("kind", "")
        self.topics = data["srgPlay"]["topics"]
        self.date = data["dateTimes"].get("startTime", None)
        self.duration = data["dateTimes"].get("realDuration", 0)

    def __repr__(self):
        topics_labels = [topic['label'] for topic in self.topics if 'label' in topic]  # Ottieni solo i label validi
        return (f"<Program(title='{self.title}', "
                f"subtitle='{self.subtitle}', "
                f"topics={topics_labels}, "
                f"productionYear={self.productionYear})>")
