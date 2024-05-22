from django.shortcuts import render
from asgiref.sync import sync_to_async
from .models import User, Consultation, Reservation, UnavailableDay
from .func import consultation_creator
import json
import datetime
import calendar
from django.http import JsonResponse, response, HttpResponse


def consultation(request):
    if request.GET.get('date'):
        get_date = request.GET.get('date')
        date = datetime.datetime.strptime(get_date, '%y/%m/%d')
        print(date)
        start_time = datetime.datetime(date.year, date.month, date.day)
        month = start_time.month
        year = start_time.year
        last_day_of_month = calendar.monthrange(year, month)
        end_time = datetime.datetime(year, month, last_day_of_month[1])
    else:
        start_time = datetime.datetime.now()
        month = start_time.month
        year = start_time.year
        last_day_of_month = calendar.monthrange(year, month)
        end_time = datetime.datetime(year, month, last_day_of_month[1])

    consultation_list = consultation_creator(start_time, end_time)

    return render(
        request,
        'consultation.html',
        {
            "consultations": consultation_list
        }
    )


def reservation_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        consultation = Consultation.objects.get(id=data.get('consultation'))
        date = data.get('date')
        member = request.user

        if not Reservation.objects.filter(member=member, date=date, consultation=consultation).exists():
            if not UnavailableDay.objects.filter(date=date, time=None).exists():
                if not UnavailableDay.objects.filter(date=date, time=consultation.start_time, capacity=None).exists():
                    if UnavailableDay.objects.filter(date=date, time=consultation.start_time, capacity=not None).exists():
                        capacity = consultation.capacity_of_members - UnavailableDay.objects.get(date=date, time=consultation.start_time).capacity
                    else:
                        capacity = consultation.capacity_of_members
                    if len(Reservation.objects.filter(consultation=consultation)) < capacity:

                        reservation = Reservation.objects.create(
                            member=member,
                            date=date,
                            consultation=consultation
                        )
                        print("done")
                        return HttpResponse("done")
                    
                    else:
                        print("consultation is full")
                        return HttpResponse("consultation is full")
                else:
                    print("consultation is unavailable")
                    return HttpResponse("consultation is unavailable")
            else: 
                print("day is unavailable")
                return HttpResponse("day is unavailable")
        else:
            print("obj already exist")
            return HttpResponse("obj already exist")