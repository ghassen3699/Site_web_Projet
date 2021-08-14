from django.shortcuts import redirect, render
from . import models, forms
from django.contrib.auth.decorators import login_required


################ django rest framework ###############
from rest_framework.decorators import api_view
from rest_framework.response import Response

from migrant_irregulier.models import Nationalite
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




@login_required(login_url='login')
def ag_grid_view(request) :
    return render(request,'operation/ag_grid.html')






@api_view(['GET'])
@login_required(login_url='login')
def json_api(request) :
    operations = models.OperationTerminer.objects.all()
    serialiser = OperationSerializer(operations, many=True)
    
    return Response(serialiser.data)





# fonction pour retourner les id des region dans une liste 
def retourner_les_id() :
    liste_des_id_regions = []
    nombre_des_regions = models.Region.objects.all().count()
    for i in range(nombre_des_regions) :
        liste_des_id_regions.append(i+1)
    
    return liste_des_id_regions




@api_view(['GET'])
@login_required(login_url='login')
def statistique(request) :
    liste_total = []
    dictionnaire = {}


    liste_des_id_regions = retourner_les_id()

    # remplissage de la liste par les noms des regions 
    regions = models.Region.objects.all().values('nom_region')
    

    for i in liste_des_id_regions :
        operations = models.OperationTerminer.objects.filter(region_id = i)
        nombre_des_operations = operations.count()    
        
        # si dans cette operation on a pas des operations 
        if nombre_des_operations > 0 :

            # calculer le nombre des operations a la terre et a la mer 
            ####################################################################################################################
            operation_terre =  models.OperationTerminer.objects.filter(region_id = i,nature_operation='Terre').count()
            operation_mer = models.OperationTerminer.objects.filter(region_id = i,nature_operation='Mer').count()
            ####################################################################################################################
            
            
            #calculer le nombre total des migrants 
            ####################################################################################################################
            nombre_des_migrants = 0
            for migrant in operations.values('nombre_des_migrants') :
                nombre_des_migrants = nombre_des_migrants + migrant['nombre_des_migrants']
            #####################################################################################################################
            
            # si on a pas des migrants 
            ##############################################################################
            if nombre_des_migrants == 0 :
                dictionnaire['nom_region'] = regions[i-1]['nom_region'],
                dictionnaire['nombre des operations total'] = nombre_des_operations,
                dictionnaire['terre'] = operation_terre,
                dictionnaire['mer'] = operation_mer,
                dictionnaire['nombre des migrants total'] = 0,
                dictionnaire['nombre des migrants tunisiens'] = 0,
                dictionnaire['nombre des migrants etrangers'] = 0
                liste_total.append(dict(dictionnaire))
            ################################################################################
            
            
            # si on a des migrants 
            #################################################################################
            else :

                # calculer le nombre des migrants tunisiens
                ######################################################
                les_migtunisiens = 0 
                id_tunisie = Nationalite.objects.values('id').filter(nom_nationalite='Tunisie') 
                for x in operations :
                    les_migrants_tunisiens = models.MigrantIrregulier.objects.filter(operationterminer = x.id , nationalite = id_tunisie[0]['id']).count()
                    les_migtunisiens = les_migtunisiens + les_migrants_tunisiens
                ######################################################


                dictionnaire['region'] =  regions[i-1]['nom_region'],
                dictionnaire['nombre des operations total'] = nombre_des_operations,
                dictionnaire['terre'] = operation_terre,
                dictionnaire['mer'] = operation_mer,
                dictionnaire['nombre des migrants total'] = nombre_des_migrants,
                dictionnaire['nombre des migrants tunisiens'] = les_migtunisiens,
                dictionnaire['nombre des migrants etrangers'] = nombre_des_migrants - les_migtunisiens
                liste_total.append(dict(dictionnaire))
            ####################################################################################

    return Response(liste_total)





@login_required(login_url='login')
def statistique_view(request) :
    return render(request,'operation/statistique.html')








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
