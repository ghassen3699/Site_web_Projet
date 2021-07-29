from django.shortcuts import redirect, render
from . import models, forms
from django.contrib.auth.decorators import login_required
from .filters import  OperationFilter
from . import filters


@login_required(login_url='login')
def home(request) :
    operations = models.OperationTerminer.objects.all()
    filter = filters.OperationFilter(request.GET, queryset=operations)
    operations = filter.qs
    prenom_agent = request.user.agent.prenom
    nom_agent = request.user.agent.nom

    return render(request,'operation/home.html',{'operations':operations,'filter':filter , 'agent_nom':nom_agent, 'agent_prenom':prenom_agent})




@login_required(login_url='login')
def creer_operations(request) :
    form = forms.OperationTerminerForm()
    if request.method == 'POST' :
        form = forms.OperationTerminerForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('operation_home')
        else :
            return render(request,'operation/creer_operation.html',{'form':form})
    return render(request,'operation/creer_operation.html',{'form':form})



@login_required(login_url='login')
def modifier_operation(request,pk) :
    operation = models.OperationTerminer.objects.get(id = pk)
    form = forms.OperationTerminerForm(instance=operation)

    if request.method == 'POST' :
        form = forms.OperationTerminerForm(request.POST,instance=operation)
        if form.is_valid() :
            form.save()
            return redirect('operation_home')
    return render(request,'operation/creer_operation.html',{'form':form})




@login_required(login_url='login')
def supprimer_operation(request, pk) :
    operation = models.OperationTerminer.objects.get(id = pk)
    if request.method == 'POST' :
        operation.delete()
        return redirect('operation_home')
    return render(request,'operation/supprimer_operation.html',{'operation':operation})


