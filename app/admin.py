from django.contrib import admin
from .models import User, Reservation, Consultation_type, Consultation, UnavailableDay

# Register your models here.

admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(Consultation_type)
admin.site.register(Consultation)
admin.site.register(UnavailableDay)
