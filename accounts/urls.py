from django.urls import path
from django.urls.conf import include
from . import views




urlpatterns = [
    #path('signup/',views.signup,name='signup'),            
    path('', include('django.contrib.auth.urls')),
    path('logout_page/',views.logout_page,name='logout_page'),
    path('profile/',views.home_page,name='account_home'),
    path('migrant/', include('migrant_irregulier.urls')),
    path('fichier_des_operations/', include('fichier_des_operations.urls')),
    path('operation/', include('operation.urls')),
    path('agent/', include('agent.urls')),
]
