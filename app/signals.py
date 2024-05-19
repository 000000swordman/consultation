from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
'''
from .models import Member_Reservation

@receiver(post_save, sender=Member_Reservation)
def add_member(sender, instance, **kwargs):
    reserv = instance.reservation
    if reserv.current_capacity < reserv.capacity_of_members:
        reserv.members.add(instance.user)
        reserv.current_capacity += 1
        reserv.save()
        print("consultation Reserv!!!")
    else:
        reserv.is_full = True
        instance.delete()
        print("capacity is full")


@receiver(post_delete, sender=Member_Reservation)
def del_member(sender, instance, **kwargs):
    reserv = instance.reservation
    reserv.members.remove(instance.user)
    reserv.current_capacity -= 1
    reserv.save()
       

'''