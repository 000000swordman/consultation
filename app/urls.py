
from django.urls import path
from . import views

urlpatterns = [
    path('consultation/<type>', views.consultation, name='consultation'),
    path('reservation/', views.reservation_api, name="reserve")
]
