from django.shortcuts import render, redirect
from django.contrib.auth import  logout

from django.core.mail import EmailMessage
from django.conf import settings

from projet_stage import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import operation
from . import forms

'''
# fonction signup 
#######################################################################################################################################################
@login_required(login_url='login')
def signup(request) :
    form = forms.UserAdminCreation()    # lire la formulaire SignupForm
    if request.method == 'POST' :      # verifier la methode de la requete
        form = forms.UserAdminCreation(request.POST)    # lire le contenu de la formulaire et l'enregistrer dans l'objet form
        if form.is_valid() :     # verifier si la formulaire est valide ou non
            form.save()              # enregistrer les donnees de la formulaire a la base de donnees 
            email = form.cleaned_data.get('email')        # enregistrer l'adresse mail de l'utilisateur dans un nouveau objet email

            email_subject = 'Activate Your Account'
            template_mail = ''
            email = EmailMessage(
                email_subject ,
                template_mail ,
                settings.EMAIL_HOST_USER ,
                [email] ,
            )
            email.send(fail_silently=False)
            messages.success(request,"Le Compte Est Creer , Verifier S'il Vous Plais L'adresse Mail ")
            return redirect('account_home')                       # retourner automatiquement a la page principale du compte 
       
        else :
            messages.warning(request,"L'adresse Mail Ou Le Mots De Passe Est Mal Creer")
            return render(request,'accounts/signup.html',{'form':form})                     # si on a un probleme au niveau de la formulaire , retourner la meme page 
    return render(request,'accounts/signup.html',{'form':form})                             # si la methode le requete est GET on affiche la meme page 
#########################################################################################################################################################
'''






# la fonction logout 
############################################################################################################################################################
@login_required(login_url='login')
def logout_page(request) :
    logout(request)      # logout du compte avec la fonction logout du django
    return redirect('login')     # retourner automatiquement a la page login du site web 
############################################################################################################################################################




@login_required(login_url='login')
def home_page(request) :
    nombre_des_operations_terminer = operation.models.OperationTerminer.objects.count()
    operations_terminer = operation.models.OperationTerminer.objects.order_by('-date_operation')[:5]
    
    return render(request,'accounts/home.html',{
        'nombre_des_operations_terminer':nombre_des_operations_terminer ,
        'operations_terminer':operations_terminer,
        }
    )


