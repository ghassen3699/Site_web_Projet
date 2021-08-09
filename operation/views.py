from lieu_de_travail.models import Region
from django.db.models.aggregates import Count
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





@login_required(login_url='login')
def afficher_operation_par_region(request) :
    liste_des_regions_id = []
    liste_des_region = []
    dictionnaire = {}
    liste = []

    regions = models.Region.objects.all().values('id')
    nombre_des_regions = regions.count()
    operations = models.OperationTerminer.objects.all()
    nombre_des_operations = operations.count()

    x = 1 
    while x <= nombre_des_regions :
        liste_des_regions_id.append(x)
        x += 1

    for i in liste_des_regions_id :
        nom_region = models.Region.objects.get(id = i)
        liste_des_region.append(nom_region.nom_region)
    

    les_operations = models.OperationTerminer.objects.all()
    for i in liste_des_regions_id :
        operations = models.OperationTerminer.objects.filter(region_id = i)
        nombre_des_operations = operations.count()

        nom = models.Region.objects.get(id = i)
        dictionnaire['nom_region'] = nom
        dictionnaire['nombre_des_operations'] = nombre_des_operations

        liste.append(dict(dictionnaire))

    
    return render(request,'operation/statistique.html',{'liste':liste})
