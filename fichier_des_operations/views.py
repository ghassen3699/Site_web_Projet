from django.core.checks import messages
from django.shortcuts import redirect, render
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from . import filters










# l'affichage de la page initiale 
@login_required(login_url='login')
def home(request) :
    fichiers = models.Fichier_Operation.objects.all()
    filter = filters.FichierFilter(request.GET, queryset=fichiers)
    fichiers = filter.qs

    
    prenom_agent = request.user.agent.prenom
    nom_agent = request.user.agent.nom
    return render(request,'fichier_des_operations/home.html',{'fichiers':fichiers,'filter':filter, 'agent_nom':nom_agent, 'agent_prenom':prenom_agent})





# creation d'une fichier d'operation
@login_required(login_url='login')
def creer_fichier_operation_view(request) :
    form = forms.FichierOperationForm()
    if request.method == 'POST' :
        form = forms.FichierOperationForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('fichiers_des_operations')
        else :
            return render(request,'fichier_des_operations/fichier_operation.html',{'form':form})
    return render(request,'fichier_des_operations/fichier_operation.html',{'form':form})




# modifier la fichier de l'operation
@login_required(login_url='login')
def modifier_fichier_operation(request,pk) :

    fichier = models.Fichier_Operation.objects.get(id = pk)
    form = forms.FichierOperationForm(instance=fichier)
    
    
    if request.method == 'POST' :
        form = forms.FichierOperationForm(request.POST ,instance=fichier)
        if form.is_valid() :
            form.save()
            return redirect('fichiers_des_operations')
    return render(request,'fichier_des_operations/modifier_fichier_des_operations.html',{'form':form})





# la supprission 
@login_required(login_url='login')
def supprimer_fichier_operation(request,pk) :

    fichier = models.Fichier_Operation.objects.get(id=pk)
    if request.method == 'POST' :
        fichier.delete()
        return redirect('fichiers_des_operations')
    return render(request,'fichier_des_operations/supprimer_fichier_operation.html',{'fichier':fichier})