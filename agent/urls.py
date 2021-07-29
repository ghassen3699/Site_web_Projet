from django.urls import path, include
from . import views



urlpatterns = [
    path('remplissage_des_donnees/',views.remplissage_donnees_agent,name='remplissage_donnees') ,
    path('profile_information/',views.profile_information,name='profile_information'),
]


