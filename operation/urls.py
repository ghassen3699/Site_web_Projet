from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='operation_home'),
    path('ajouter_operation/',views.creer_operations,name='ajouter_operation'),
    path('modifier_operation/<str:pk>/',views.modifier_operation,name='modifier_operation'),
    path('supprimer_operation/<str:pk>/',views.supprimer_operation,name='supprimer_operation'),
    path('statistique/',views.statistique,name='statistique')
]
