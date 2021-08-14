from django.shortcuts import redirect, render
from . import models, forms
from django.contrib.auth.decorators import login_required


################ django rest framework ###############
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import OperationSerializer
from lieu_de_travail.serializers import  SerializeRegion



@login_required(login_url='login')
def creer_operations(request) :
    
    form = forms.OperationTerminerForm()

    if request.method == 'POST' :

        form = forms.OperationTerminerForm(request.POST)

        if form.is_valid() :
            return redirect('ajouter_operation')

        else :
            return render(request,'operation/creer_operation.html',{'form':form})

    return render(request,'operation/creer_operation.html',{'form':form})



'''

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

'''



'''
@login_required(login_url='login')
def supprimer_operation(request, pk) :
    operation = models.OperationTerminer.objects.get(id = pk)
    if request.method == 'POST' :
        operation.delete()
        return redirect('operation_home')
    return render(request,'operation/supprimer_operation.html',{'operation':operation})

'''





def ag_grid_view(request) :
    return render(request,'operation/ag_grid.html')






@api_view(['GET'])
def json_api(request) :
    operations = models.OperationTerminer.objects.all()
    serialiser = OperationSerializer(operations, many=True)
    
    return Response(serialiser.data)






@api_view(['GET'])
def statistique(request) :
    liste_total = []
    liste_des_id_regions = []
    liste_des_regions = []
    dictionnaire = {}

    nombre_des_regions = models.Region.objects.all().count()

    for i in range(nombre_des_regions) :
        liste_des_id_regions.append(i+1)
    
    for x in liste_des_id_regions :
        nom_region = models.Region.objects.get(id = x)
        nom_region_ser = SerializeRegion(nom_region,many=False)
        liste_des_regions.append(nom_region_ser.data)


    for i in liste_des_id_regions :

        operations = models.OperationTerminer.objects.filter(region_id = i)
        nombre_des_operations = operations.count()    
        
        if nombre_des_operations == 0 : 
            pass

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
                
                dictionnaire['nom_region'] = liste_des_regions[i-1]['nom_region'],
                dictionnaire['nombre des operations total'] = nombre_des_operations,
                dictionnaire['terre'] = operation_terre,
                dictionnaire['mer'] = operation_mer,
                dictionnaire['nombre des migrants total'] = nombre_des_migrants,
                dictionnaire['nombre des migrants tunisiens'] = nombre_des_migrants,
                dictionnaire['nombre des migrants etrangers'] = nombre_des_migrants
                liste_total.append(dict(dictionnaire))
                
            else :
                
                dictionnaire['region'] = liste_des_regions[i-1]['nom_region'],
                dictionnaire['nombre des operations total'] = nombre_des_operations,
                dictionnaire['terre'] = operation_terre,
                dictionnaire['mer'] = operation_mer,
                dictionnaire['nombre des migrants total'] = nombre_des_migrants,
                dictionnaire['nombre des migrants tunisiens'] = les_migtunisiens,
                dictionnaire['nombre des migrants etrangers'] = nombre_des_migrants - les_migtunisiens
                liste_total.append(dict(dictionnaire))

    return Response(liste_total)






def statistique_view(request) :
    return render(request,'operation/statistique.html')