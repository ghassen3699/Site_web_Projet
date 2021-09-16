import agent
from django.shortcuts import render, redirect
from django.contrib.auth import  logout

from django.core.mail import EmailMessage
from django.conf import settings

from projet_stage import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import operation
from . import forms
from agent.forms import AgentForm
from agent.models import Agent





def ajouter_compte(request) :
    user_form = forms.UserAdminCreation()
    agent_form = AgentForm()
    if request.method == 'POST' :
        user_form = forms.UserAdminCreation(request.POST)
        agent_form = AgentForm(request.POST)
        if user_form.is_valid() and agent_form.is_valid() :
            user = user_form.save()
            Agent.objects.create(
                account_user = user ,
                nom = agent_form.cleaned_data.get('nom') ,
                prenom = agent_form.cleaned_data.get('prenom') ,
                age = agent_form.cleaned_data.get('age') ,
                numero_telephone = agent_form.cleaned_data.get('numero_telephone') ,
                adresse = agent_form.cleaned_data.get('adresse') ,
                code_postal = agent_form.cleaned_data.get('code_postal') ,
                genre = agent_form.cleaned_data.get('genre') ,
                grade_de_travail_fk = agent_form.cleaned_data.get('grade_de_travail_fk') ,
                numero_cin = agent_form.cleaned_data.get('numero_cin') ,
            )
            messages.success(request,'Le Compte Est Creer')
            return redirect('account_home')
        else :
            messages.success(request,"Il y'a un erreur au niveau de votre formulaire")
    return render(request,'accounts/signup.html',{'user_form':user_form,'agent_form':agent_form})




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


