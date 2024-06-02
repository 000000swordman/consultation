import datetime
import copy
from .models import Consultation, UnavailableDay, Reservation

def consultation_creator(start: datetime, end: datetime):
    consultation_list = []
    start_day = start.day
    end_day = end.day
    month = start.month
    year = start.year
    reservation_list = Reservation.objects.filter(date__range=[start, end]).order_by('date')
    unavailable_list = UnavailableDay.objects.filter(date__range=[start, end]).order_by('date')
    unavailable_capacity_dict = {}
    consultations = Consultation.objects.all()
    consultation_dict = {}

    for consultation in consultations:
        weekday = consultation.day
        if not weekday in consultation_dict:
            consultation_dict[weekday] = {}
        consultation_dict[weekday][consultation.start_time] = consultation
    

    for unavailable in unavailable_list:
        r_date = unavailable.date.day
        if unavailable.time == None and unavailable.capacity == None:
            unavailable_capacity_dict[r_date] = None
             
        elif unavailable.time == None and unavailable.capacity != None:
            unavailable_capacity_dict[r_date] = {'all': unavailable.capacity}
            
        else:
            con = unavailable.time
            if not r_date in unavailable_capacity_dict:
                unavailable_capacity_dict[r_date] = {}
            if not con in unavailable_capacity_dict[r_date]:
                unavailable_capacity_dict[r_date][con] = 0
            if unavailable.capacity == None:
                unavailable_capacity_dict[r_date][con] = None
            else:
                unavailable_capacity_dict[r_date][con] += unavailable.capacity

    for reservation in reservation_list:
        r_date = reservation.date.day
        if r_date in unavailable_capacity_dict and unavailable_capacity_dict[r_date] == None:
            continue
        con = reservation.time
        if not r_date in unavailable_capacity_dict:
            unavailable_capacity_dict[r_date] = {}
        if not con in unavailable_capacity_dict[r_date]:
            unavailable_capacity_dict[r_date][con] = 0
        if not unavailable_capacity_dict[r_date][con] == None:
            unavailable_capacity_dict[r_date][con] += 1

    
    print('**************************unavailable_capacity_dict**********************************')
    for x in unavailable_capacity_dict:
        print ('        ',x,':',unavailable_capacity_dict[x])
    print('*************************************************************************************')
    print('**************************consultation_dict******************************************')
    for x in consultation_dict:
        print ('        ',x,':',consultation_dict[x])
    print('*************************************************************************************')



    for x in range(start_day, end_day):
        time = datetime.datetime(year, month, x)
        weekday = time.strftime("%A")
        obj_list = []
        if weekday in consultation_dict:
            consultations_of_w = consultation_dict[weekday]
            for y in consultations_of_w:
                obj = {}
                obj["obj"] = copy.deepcopy(consultations_of_w[y])
                if x in unavailable_capacity_dict:
                    u_day = unavailable_capacity_dict[x]
                    if u_day == None:
                        obj["obj"].capacity_of_members = 0
                    else:
                        if obj["obj"].start_time in u_day:
                            if u_day[obj['obj'].start_time] == None:
                                obj["obj"].capacity_of_members = 0
                            else:
                                obj["obj"].capacity_of_members -= u_day[consultations_of_w[y].start_time]
                        if 'all' in u_day:
                            obj["obj"].capacity_of_members -= u_day['all']
                obj_list.append(obj["obj"])
                print(obj['obj'])
                
                
        
        
        consultation = {
            'consultation': obj_list,
            'date': time,

        }
        consultation_list.append(consultation)
    for r in consultation_dict:
            print(consultation_dict[r], "77777")
    return consultation_list