from accounts import models
from django.contrib.auth import get_user_model
from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm






# la formulaire de creation d'un compte a partir de l'admin
#######################################################################################################
class UserAdminCreation(UserCreationForm) :
    class Meta :
        model = get_user_model()                     # ajouter le model user 
        fields = ['email']           #   ajouter les fields (NB: on ajoute juste l'email car le field password1 et password2 est deja ajouter par defaut)
#######################################################################################################
