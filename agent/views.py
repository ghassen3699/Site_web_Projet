from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms


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

    return render(request,'agent/home_agent.html',{'profile_infos':profile_infos})


