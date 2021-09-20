from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),    
    path('logout_page/',views.logout_page,name='logout_page'),
    path('profile/',views.home_page,name='account_home'),
    path('migrant/', include('migrant_irregulier.urls')),
    path('operation/', include('operation.urls')),
    path('agent/', include('agent.urls')),
    path('ajouter_compte/',views.ajouter_compte, name='Ajouter_Compte'),

    #2
    path('password_reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_message.html'),name='password_reset_done'),    
   
    #3
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_confirm.html'),name='password_reset_confirm'),   
    #1
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name="password_reset"), 
    #4
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'),name='password_reset_complete'),    
]
