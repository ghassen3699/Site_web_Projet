from accounts.views import home_page
from django.urls import path
from . import views






urlpatterns = [
    path('all_files/',views.home,name='fichiers_des_operations'),
    path('create/',views.creer_fichier_operation_view,name='creer_fichier'),
    path('update/<str:pk>/',views.modifier_fichier_operation,name='modifier_fichier'),
    path('delete/<str:pk>/',views.supprimer_fichier_operation,name='supprimer_fichier'),
    path('api/',views.fichier_api,name='api'),


]
