from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='operation_home'),
    path('ajouter_operation/',views.creer_operations,name='ajouter_operation'),
    path('modifier_operation/<str:pk>/',views.modifier_operation,name='modifier_operation'),
    path('supprimer_operation/<str:pk>/',views.supprimer_operation,name='supprimer_operation'),
    path('statistique/',views.afficher_operation_par_region,name='statistique'),
    path('ag_grid/',views.ag_grid_view,name='ag_grid')
]
