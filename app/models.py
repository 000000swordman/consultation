from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(('first name'), max_length=150, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    email = models.EmailField(('email address'), blank=True)
    password = models.CharField(('password'), max_length=128)

    def __str__(self):
        return self.username


class Consultation_type(models.Model):
    type = models.CharField(('reservation type'), max_length=150)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.type


class Consultation(models.Model):
    class Weekday(models.TextChoices):
        mon = "Monday", "Monday"
        tue = "Tuesday", "Tuesday"
        wed = "Wednesday", "Wednesday"
        thu = "Thursday", "Thursday"
        fri = "Friday", "Friday"
        sun = "Sunday", "Sunday"

    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.ForeignKey(Consultation_type, on_delete=models.CASCADE)
    day = models.CharField(max_length=10,default='sun ', choices=Weekday.choices)
    capacity_of_members = models.IntegerField(default=10)


    def __str__(self):
        return self.day +' at '+ str(self.start_time) + ' for ' + str(self.type) + ' Consultation.'


class Reservation(models.Model):
    date = models.DateField()
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    member = models.ForeignKey(User, related_name='member', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.date) +' '+ str(self.consultation) +' '+ str(self.member)
    
class UnavailableDay(models.Model):
    date = models.DateField()
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)        
    all_day = models.BooleanField(default=False)
