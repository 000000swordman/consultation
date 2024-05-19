
from django.urls import path
from . import views

urlpatterns = [
    path('consultation/', views.consultation, name='consultation'),
    path('reservation/', views.reservation_api, name="reserve")
]
