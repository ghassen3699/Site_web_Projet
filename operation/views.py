from lieu_de_travail.models import Region
from django.db.models.aggregates import Count
from django.shortcuts import redirect, render
from . import models, forms
from django.contrib.auth.decorators import login_required
from . import filters
from migrant_irregulier.models import Nationalite
from migrant_irregulier.forms import MigrantIrregulierForm

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
    form_migrant = MigrantIrregulierForm()
    if request.method == 'POST' :
        form = forms.OperationTerminerForm(request.POST)
        form_migrant = MigrantIrregulierForm(request.POST)
        if form.is_valid() :
            if form_migrant.is_valid() :
                form.save()
                form_migrant.save()
                return redirect('operation_home')
        else :
            return render(request,'operation/creer_operation.html',{'form':form,'form_migrant':form_migrant})
    return render(request,'operation/creer_operation.html',{'form':form,'form_migrant':form_migrant})



@login_required(login_url='login')
def modifier_operation(request,pk) :
    operation = models.OperationTerminer.objects.get(id = pk)
    form = forms.OperationTerminerForm(instance=operation)

    if request.method == 'POST' :
        form = forms.OperationTerminerForm(request.POST,instance=operation)
        if form.is_valid() :
            form.save()
            return redirect('operation_home')
    return render(request,'operation/modifier_operation.html',{'form':form})




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
    liste_des_nationalite_id = []
    liste_des_region = []
    dictionnaire = {}
    liste = []

    regions = models.Region.objects.all().values('id')
    nombre_des_regions = regions.count()
    operations = models.OperationTerminer.objects.all()
    


    nombre_nationalites = Nationalite.objects.all().values('id').count()

    y = 1 
    while y <= nombre_nationalites :
        liste_des_nationalite_id.append(y)
        y += 1
    


    x = 1 
    while x <= nombre_des_regions :
        liste_des_regions_id.append(x)
        x += 1

    

    for i in liste_des_regions_id :
        nom_region = models.Region.objects.get(id = i)
        liste_des_region.append(nom_region.nom_region)
    

    

    for i in liste_des_regions_id :
        operations = models.OperationTerminer.objects.filter(region_id = i)
        nombre_des_operations = operations.count()
        

        # tester si il y'a des operations 
        # 1 ) on a pas des operations dans cette region 
        if nombre_des_operations == 0 :
            pass
        
        
        # 2) on a des operations dans cette region
        else :
            operation_terre =  models.OperationTerminer.objects.filter(region_id = i,nature_operation='Terre').count()
            operation_mer = models.OperationTerminer.objects.filter(region_id = i,nature_operation='Mer').count()
            
            les_migtunisiens = 0 
            for x in operations :
                les_migrants_tunisiens = models.MigrantIrregulier.objects.filter(operationterminer = x.id , nationalite_id = 1).count()
                les_migtunisiens = les_migtunisiens + les_migrants_tunisiens
                

            nombre_des_migrants = 0

            for migrant in operations.values('nombre_des_migrants') :
                nombre_des_migrants = nombre_des_migrants + migrant['nombre_des_migrants']
                
            if nombre_des_migrants == 0 :
                nom = models.Region.objects.get(id = i)
                dictionnaire['nom_region'] = nom
                dictionnaire['nombre_des_operations'] = nombre_des_operations
                dictionnaire['les_operations'] = operations
                dictionnaire['les_migrants_tunisien'] = nombre_des_migrants
                dictionnaire['les_migrants_non_tunisien'] = nombre_des_migrants 
                liste.append(dict(dictionnaire))
            
            
            else :
                nom = models.Region.objects.get(id = i)
                dictionnaire['nom_region'] = nom
                dictionnaire['nombre_des_operations'] = nombre_des_operations
                dictionnaire['les_operations'] = operations
                dictionnaire['les_migrants_tunisien'] = les_migtunisiens
                dictionnaire['les_migrants_non_tunisien'] = nombre_des_migrants - les_migtunisiens
                dictionnaire['operation_terre'] = operation_terre
                dictionnaire['operation_mer'] = operation_mer
                liste.append(dict(dictionnaire))

    
    return render(request,'operation/ag_grid.html',{'liste':liste})





def ag_grid_view(request) :
    return render(request,'operation/ag_grid.html')

