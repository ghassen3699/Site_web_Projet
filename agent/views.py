from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages



'''
# remplissage des donnees 
@login_required(login_url='login')
def remplissage_donnees_agent(request) :
    prenom_user = request.user.agent.prenom
    form = forms.AgentForm()
    if request.method == 'POST' :
        form = forms.AgentForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request,'{} : vos donnees sont enregistrées'.format(prenom_user))
            return redirect('account_home')
        else :
            messages.warning(request,"{} Il y'a Une erreur au Niveau du remplissage des donnees".format(prenom_user))
            return render(request,'agent/creer_agent.html',{'form':form})
    return render(request,'agent/creer_agent.html',{'form':form})

'''





def profile_information(request) :
    profile_infos = request.user.agent
    
    form = forms.AgentForm(instance=profile_infos)
    '''
    if request.method == 'POST' :
        form = forms.AgentForm(request.POST,instance=profile_information)
        if form.is_valid() :
            return redirect('account_home')
    '''
    return render(request,'agent/home_agent.html',{'form':form})



