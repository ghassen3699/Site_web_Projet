from django.urls import path, include
from . import views


urlpatterns = [
    #path('ajouter_migrant/',views.ajouter_migrant,name='ajouter_migrant'),
    path('',views.home,name='page_home_migrant'),
    #path('update/<str:pk>/',views.modifier_migrant,name='modifier_migrant'),
    #path('delete/<str:pk>/',views.supprimer_migrant,name='suprimer_migrant'),
    path('test_migrant/',views.migrant_irregulier_api,name='api'),
]
