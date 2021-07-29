from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from operation.models import OperationTerminer

# remplissage des donnees 
@login_required(login_url='login')
def remplissage_donnees_agent(request) :
    form = forms.AgentForm()
    if request.method == 'POST' :
        form = forms.AgentForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('account_home')
        else :
            return render(request,'agent/creer_agent.html',{'form':form})
    return render(request,'agent/creer_agent.html',{'form':form})




def profile_information(request) :
    profile_infos = request.user.agent
    email = request.user.email
    prenom_agent = request.user.agent.prenom
    nom_agent = request.user.agent.nom

    operation_user = OperationTerminer.objects.filter(agent_fk = request.user.id)[:8]
    operation_user_nombre = OperationTerminer.objects.filter(agent_fk = request.user.id).count()
    form = forms.AgentForm(instance=profile_infos)
    if request.method == 'POST' :
        form = forms.AgentForm(request.POST,instance=profile_information)
        if form.is_valid() :
            return redirect('account_home')

    return render(request,'agent/home_agent.html',{'profile_infos':profile_infos,'prenom_agent':prenom_agent, 'nom_agent':nom_agent,'form':form, 'email':email,'operation_user':operation_user,'operation_user_nombre':operation_user_nombre})



