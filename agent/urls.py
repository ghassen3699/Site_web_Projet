from django.urls import path, include
from . import views



urlpatterns = [
    path('profile_information/',views.profile_information,name='profile_information'),
]


