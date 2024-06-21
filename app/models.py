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
    room = models.ManyToManyField('Room', blank=True)

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
        return self.day +' at '+ str(self.start_time)


class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    member = models.ForeignKey(User, related_name='member', on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Consultation_type, on_delete=models.CASCADE, null=True)
    meeting = models.ForeignKey(Consultation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.date) +' '+ str(self.time) +' '+ str(self.member)
    
class UnavailableDay(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    capacity = models.SmallIntegerField(null=True, blank=True)
    type = models.ForeignKey(Consultation_type, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.date) +' '+ str(self.time)

class Room(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    class Type(models.TextChoices):
        consultation = 'Consultation', 'Consultation'
        manager_meeting = "Managers meeting", "Managers meeting"

    type = models.CharField(max_length=50, default='con ', choices=Type.choices)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.type)
