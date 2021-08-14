from django.urls import path
from . import views


urlpatterns = [
    
    path('ajouter_operation/',views.creer_operations,name='ajouter_operation'),
    #path('modifier_operation/<str:pk>/',views.modifier_operation,name='modifier_operation'),
    #path('supprimer_operation/<str:pk>/',views.supprimer_operation,name='supprimer_operation'),
    path('statistique_api/',views.statistique,name='statistique'),
    path('statistique/',views.statistique_view,name='statistique'),
    path('',views.ag_grid_view,name='operation_home'),
   
    path('json_api/',views.json_api,name='json_api'),
    
]
