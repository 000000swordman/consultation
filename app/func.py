import datetime
import copy
from .models import Consultation, UnavailableDay, Reservation, Meeting
from django.db.models import F


def consultation_creator(start: datetime, end: datetime, type):
    consultation_list = []
    start_day = start.day
    end_day = end.day
    month = start.month
    year = start.year
    reservation_list = Reservation.objects.filter(type=type, date__range=[start, end]).order_by('date')
    unavailable_list = UnavailableDay.objects.filter(type=type, date__range=[start, end]).order_by(
        'date', F('time').desc(nulls_last=True), F('capacity').desc(nulls_last=True),)
    meetigs = Meeting.objects.filter(date__range=[start, end]).order_by('date')
    meetig_dict = {}
    unavailable_capacity_dict = {}
    consultations = Consultation.objects.filter(type=type)
    consultation_dict = {}
    print(consultations)

    for meetig in meetigs:
        day = meetig.date.day
        room = meetig.room
        start_time = meetig.start_time
        end_time = meetig.end_time
        if day not in meetig_dict:
            meetig_dict[day] = {}
        if room not in meetig_dict[day]:
            meetig_dict[day][room] = {}
        meetig_dict[day][room][start_time] = [start_time, end_time]


    for consultation in consultations:

        weekday = consultation.day
        c_type = consultation.type
        if weekday not in consultation_dict:
            consultation_dict[weekday] = {}
        if c_type not in consultation_dict[weekday]:
            consultation_dict[weekday][c_type] = {}
        consultation_dict[weekday][c_type][consultation.start_time] = consultation


    for unavailable in unavailable_list:
        r_date = unavailable.date.day
        if unavailable.time is None and unavailable.capacity is None:
            unavailable_capacity_dict[r_date] = None

        elif unavailable.time is None and unavailable.capacity is not None:
            unavailable_capacity_dict[r_date] = {'all': unavailable.capacity}

        else:
            con = unavailable.time
            c_type = unavailable.type
            if r_date not in unavailable_capacity_dict:
                unavailable_capacity_dict[r_date] = {}
            if c_type not in unavailable_capacity_dict[r_date]:
                unavailable_capacity_dict[r_date][c_type] = {}
            if con not in unavailable_capacity_dict[r_date][c_type]:
                unavailable_capacity_dict[r_date][c_type][con] = 0
            if unavailable.capacity is None:
                unavailable_capacity_dict[r_date][c_type][con] = None
            else:
                unavailable_capacity_dict[r_date][c_type][con] += unavailable.capacity

    for reservation in reservation_list:
        r_date = reservation.date.day
        if r_date in unavailable_capacity_dict and unavailable_capacity_dict[r_date] is None:
            continue
        con = reservation.time
        c_type = reservation.type
        if r_date not in unavailable_capacity_dict:
            unavailable_capacity_dict[r_date] = {}
        if c_type not in unavailable_capacity_dict[r_date]:
            unavailable_capacity_dict[r_date][c_type] = {}
        if con not in unavailable_capacity_dict[r_date][c_type]:
            unavailable_capacity_dict[r_date][c_type][con] = 0
        if unavailable_capacity_dict[r_date][c_type][con] is not None:
            unavailable_capacity_dict[r_date][c_type][con] += 1

    print('**************************unavailable_capacity_dict**********************************')
    for x in unavailable_capacity_dict:
        print('        ', x, ':', unavailable_capacity_dict[x])
    print('*************************************************************************************')
    print('**************************consultation_dict******************************************')
    for x in consultation_dict:
        print('        ', x, ':', consultation_dict[x])
    print('*************************************************************************************')
    print('**************************meeting_dict******************************************')
    for x in meetig_dict:
        print('        ', x, ':', meetig_dict[x])
    print('*************************************************************************************')


    for x in range(start_day, end_day):
        time = datetime.datetime(year, month, x)
        weekday = time.strftime("%A")
        obj_list = []
        if weekday in consultation_dict:
            consultations_of_w = consultation_dict[weekday]
            for y in consultations_of_w:
                for z in consultations_of_w[y]:
                    obj = copy.deepcopy(consultations_of_w[y][z])
                    if x in unavailable_capacity_dict:
                        u_day = unavailable_capacity_dict[x]
                        if u_day is None:
                            obj.capacity_of_members = 0
                        else:
                            for i in u_day:
                                if obj.type == i:
                                    if obj.start_time in u_day[i]:
                                        if u_day[i][obj.start_time] is None:
                                            obj.capacity_of_members = 0
                                        else:
                                            obj.capacity_of_members -= u_day[i][obj.start_time]
                                if 'all' in u_day:
                                    obj.capacity_of_members -= u_day['all']
                    rooms = obj.type.room.all()
                    rooms_capacity = len(rooms)
                    m_capacity = 0
                    if x in meetig_dict:
                        for m in meetig_dict[x]:
                            if m in rooms:
                                for p in meetig_dict[x][m]:
                                    start_meeting = meetig_dict[x][m][p][0]
                                    end_meeting = meetig_dict[x][m][p][1]
                                    if obj.start_time <= start_meeting <= obj.end_time or obj.start_time <= end_meeting <= obj.end_time or start_meeting < obj.start_time and end_meeting > obj.end_time:
                                        m_capacity += 1
                    final_rooms_capacity = rooms_capacity - m_capacity
                    if final_rooms_capacity < obj.capacity_of_members:
                        obj.capacity_of_members = final_rooms_capacity

                    obj_list.append(obj)

        consultation = {
            'consultation': obj_list,
            'date': time,
        }
        consultation_list.append(consultation)

    return consultation_list
