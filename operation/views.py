from django.db.models.functions import Cast
from django.db.models.aggregates import Sum
from django.db.models.fields import IntegerField
from django.shortcuts import redirect, render
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Q

################ django rest framework ###############
from rest_framework.decorators import api_view
from rest_framework.response import Response

from migrant_irregulier.models import Nationalite
from .serializers import OperationSerializer
from lieu_de_travail.serializers import  SerializeRegion
from lieu_de_travail.models import Region

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from projet_stage import settings
user = get_user_model()





@login_required(login_url='login')
def creer_operations(request) :
    
    form = forms.OperationTerminerForm()

    if request.method == 'POST' :
        form = forms.OperationTerminerForm(request.POST)

        if form.is_valid() :
            form.save()
            operation = form.cleaned_data.get('nom_operation')
            messages.success(request,'{} est enregistrer'.format(operation))
            
            
            return redirect('ajouter_operation')
        else :
            messages.success(request,"Il y'a une erreur au niveau de votre formulaire")

    return render(request,'operation/creer_operation.html',{'form':form})




@login_required(login_url='login')
def ag_grid_view(request) :
    return render(request,'operation/ag_grid.html')






@api_view(['GET'])
@login_required(login_url='login')
def json_api(request) :
    dictionnaire = {}
    liste = []
    operations = models.OperationTerminer.objects.all()
    serialiser = OperationSerializer(operations, many=True) 

    for i in (serialiser.data) :

        region = Region.objects.get(id = i['region'])
        region_ser = SerializeRegion(region, many=False)
        dictionnaire['region'] =  region_ser.data['nom_region']
        dictionnaire['nom_operation'] = i['nom_operation'] ,
        dictionnaire['date_operation'] = i['date_operation'] ,
        dictionnaire['nombre_des_migrants'] = i['nombre_des_migrants'] , 
        dictionnaire['nature_operation'] = i['nature_operation'] ,
        liste.append(dict(dictionnaire))
    
    
    return Response(liste)





# fonction pour retourner les id des region dans une liste 
def retourner_les_id() :
    liste_des_id_regions = []
    nombre_des_regions = models.Region.objects.all().count()
    for i in range(nombre_des_regions) :
        liste_des_id_regions.append(i+1)
    
    return liste_des_id_regions




@login_required(login_url='login')
def statistique_view(request) :
    return render(request,'operation/statistique.html')






'''  
@api_view(['GET'])
@login_required(login_url='login')
def test_agregation(request) :

    l = []
    liste = []
    dictionnaire = {}
    
    id_tunisie = Nationalite.objects.values('id').filter(nom_nationalite='Tunisie') 
    id_nationalite = Nationalite.objects.values_list('id')
    for x in range(len(id_nationalite)) :
        l.append(x+1)
    l.remove(id_tunisie[0]['id'])
    
    
    region_par_operations = (models.OperationTerminer.objects
        .values('region__nom_region')
        .annotate(
            nombre_des_operation_total= Count('region__operationterminer'),
            terre = Count('region__operationterminer',filter=Q(region__operationterminer__nature_operation='Terre')),
            mer = Count('region__operationterminer',filter=Q(nature_operation='Mer')),
            
        )
        
    )
    print(region_par_operations)

    region_par_migrant = (models.OperationTerminer.objects
        .values('region__nom_region')
        .annotate(
            nombre_des_migrant_total = Cast(Count('nombre_des_migrants'),output_field=IntegerField()),
            nombre_des_migrants_tunisien = Cast(Count('les_migrants',filter=Q(les_migrants__nationalite__nom_nationalite = 'Tunisie')),output_field=IntegerField()),
            nombre_des_migrants_etranger = Cast(Count('les_migrants',filter=Q(les_migrants__nationalite__in = l)),output_field=IntegerField())
        )
        
    )
    print(region_par_migrant)

    for i in region_par_operations :
        for j in region_par_migrant :
            if i['region__nom_region'] == j['region__nom_region'] :
                dictionnaire['region'] = i['region__nom_region']
                dictionnaire['nombre_des_operations'] = i['nombre_des_operation_total']
                dictionnaire['terre'] = i['terre']
                dictionnaire['mer'] = i['mer']
                dictionnaire['nombre_des_migrant'] = j['nombre_des_migrant_total']
                dictionnaire['nombre_des_migrants_tunisien'] = j['nombre_des_migrants_tunisien']
                dictionnaire['nombre_des_migrants_etranger'] = j['nombre_des_migrants_etranger']
        liste.append(dict(dictionnaire))


    return Response(liste)
    
'''




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
                dictionnaire['region'] = regions[i-1]['nom_region'],
                dictionnaire['nombre_des_operations'] = nombre_des_operations,
                dictionnaire['terre'] = operation_terre,
                dictionnaire['mer'] = operation_mer,
                dictionnaire['nombre_des_migrant'] = 0,
                dictionnaire['nombre_des_migrants_tunisien'] = 0,
                dictionnaire['nombre_des_migrants_etranger'] = 0
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
                dictionnaire['nombre_des_operations'] = nombre_des_operations,
                dictionnaire['terre'] = operation_terre,
                dictionnaire['mer'] = operation_mer,
                dictionnaire['nombre_des_migrant'] = nombre_des_migrants,
                dictionnaire['nombre_des_migrants_tunisien'] = les_migtunisiens,
                dictionnaire['nombre_des_migrants_etranger'] = nombre_des_migrants - les_migtunisiens
                liste_total.append(dict(dictionnaire))
            ####################################################################################

    return Response(liste_total)







@login_required(login_url='login')
def modifier_operation(request,pk) :
    operation = models.OperationTerminer.objects.get(id = pk)
    form = forms.OperationTerminerForm(instance=operation)

    if request.method == 'POST' :
        form = forms.OperationTerminerForm(request.POST,instance=operation)
        if form.is_valid() :
            form.save()
            messages.success(request,'{} est modifier'.format(operation))
            return redirect('modifier_operations')
        else :
            messages.success(request,"Il y'a une erreur au niveau de votre formulaire")

    return render(request,'operation/modifier_operation.html',{'form':form})











@login_required(login_url='login')
def supprimer_operation(request, pk) :
    operation = models.OperationTerminer.objects.get(id = pk)
    if request.method == 'POST' :
        operation.delete()
        return redirect('modifier_operations')
    return render(request,'operation/supprimer_operation.html',{'operation':operation})










def liste_modification(request) :
    operations = models.OperationTerminer.objects.all()

    if request.method == "POST" :
        recherche = request.POST['recherche']
        operation = models.OperationTerminer.objects.filter(nom_operation__icontains = recherche)
        if not operation.exists() :
            operation = models.OperationTerminer.objects.filter(date_operation__icontains = recherche)
        
        if not operation.exists() :
            operation = models.OperationTerminer.objects.filter(nombre_des_migrants__icontains = recherche)
        
        if not operation.exists() :
            operation = models.OperationTerminer.objects.filter(region__nom_region__icontains = recherche)
        
        if not operation.exists() :
            operation = models.OperationTerminer.objects.filter(province__nom_province__icontains = recherche)
        

        return render(request,'operation/liste_modification.html',{'operation':operation})

    else :
        operations = models.OperationTerminer.objects.all()
        return render(request,'operation/liste_modification.html',{'operations':operations})



