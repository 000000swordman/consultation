import datetime
from .models import Consultation

def consultation_creator(start: datetime, end: datetime):
    consultation_list = []
    start_day = start.day
    end_day = end.day
    month = start.month
    year = start.year


    for x in range(start_day, end_day):
        time = datetime.datetime(year, month, x)
        weekday = time.strftime("%A")
        obj = Consultation.objects.filter(day=weekday)
        consultation = {
            'consultation': obj,
            'date': time
        }
        consultation_list.append(consultation)

    return consultation_list