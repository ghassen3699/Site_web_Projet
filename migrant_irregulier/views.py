from rest_framework.decorators import api_view
from rest_framework.response import Response
from migrant_irregulier.serializers import Serializer_Migrant, Serializer_Nationalite
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='login')
def ajouter_migrant(request) :
    form = forms.MigrantIrregulierForm()
    if request.method == 'POST' :
        form = forms.MigrantIrregulierForm(request.POST)
        if form.is_valid() :
            form.save()
            migrant_nom = form.cleaned_data.get('nom')
            migrant_prenom = form.cleaned_data.get('prenom')
            messages.success(request,'{} {} est enregistrer'.format(migrant_nom,migrant_prenom))
            return redirect('ajouter_migrant')
        else :
            messages.success(request,"Il y'a une erreur au niveau de votre formulaire")
            return render(request,'migrant_irregulier/ajouter_migrant.html',{'form':form})
    return render(request,'migrant_irregulier/ajouter_migrant.html',{'form':form})







@login_required(login_url='login')
def modifier_migrant(request,pk) :
    migrant = models.MigrantIrregulier.objects.get(id = pk)
    form = forms.MigrantIrregulierForm(instance=migrant)

    if request.method == 'POST' :
        form = forms.MigrantIrregulierForm(request.POST ,instance=migrant)
        if form.is_valid() :
            form.save()
            migrant_nom = form.cleaned_data.get('nom')
            migrant_prenom = form.cleaned_data.get('prenom')
            messages.success(request,'{} {} est modifier'.format(migrant_nom,migrant_prenom))

            return redirect('modifier_migrants')
        else :
            messages.success(request,"Il y'a une erreur au niveau de votre formulaire")
            return render(request,'migrant_irregulier/modifier_migrant.html',{'form':form})
    return render(request,'migrant_irregulier/modifier_migrant.html',{'form':form})




@login_required(login_url='login')
def supprimer_migrant(request,pk) :
    migrant = models.MigrantIrregulier.objects.get(id=pk)

    if request.method == 'POST' :
        migrant.delete()
        return redirect('modifier_migrants')
    return render(request,'migrant_irregulier/supprimer_migrant.html',{'migrant':migrant})



@api_view(['GET'])
@login_required(login_url='login')
def migrant_irregulier_api(request) :
    dictionnaire = {}
    liste = []
    les_migrants = models.MigrantIrregulier.objects.all()
    les_migrants_ser = Serializer_Migrant(les_migrants, many = True)

    print(les_migrants_ser.data[0]['nationalite'])

    
    for i in (les_migrants_ser.data) :
        nationalite = models.Nationalite.objects.get(id = i['nationalite'])
        nationalite_ser = Serializer_Nationalite(nationalite, many=False)
        
        dictionnaire['Nationalite'] = nationalite_ser.data['nom_nationalite'] ,
        dictionnaire['CIN'] = i['numero_cin'] ,
        dictionnaire['Nom'] = i['nom'] ,
        dictionnaire['Prenom'] = i['prenom'] , 
        dictionnaire["L'age"] = i['age'] ,
        dictionnaire['Genre'] = i['sexe'] ,
        dictionnaire['N°Telephone'] = i['numero_telephone'] ,
        dictionnaire['N°Passport'] = i['numero_passport'] ,
        dictionnaire['Date'] = i['capter_date'] ,
        
        liste.append(dict(dictionnaire))
    
    return Response(liste)





@login_required(login_url='login')
def home(request) :
    return render(request,'migrant_irregulier/home.html')




def modifier_liste_migrant(request) :

    migrants = models.MigrantIrregulier.objects.all()
    if request.method == "POST" :
        recherche = request.POST['recherche']
        migrant = models.MigrantIrregulier.objects.filter(numero_cin__contains = recherche)

        if not migrant.exists() :
            migrant = models.MigrantIrregulier.objects.filter(nom__contains = recherche)

        if not migrant.exists() :
            migrant = models.MigrantIrregulier.objects.filter(prenom__contains = recherche)

        if not migrant.exists() :
            migrant = models.MigrantIrregulier.objects.filter(age__contains = recherche)

        if not migrant.exists() :
            migrant = models.MigrantIrregulier.objects.filter(numero_passport__contains = recherche)

        if not migrant.exists() :
            migrant = models.MigrantIrregulier.objects.filter(sexe__contains = recherche)

        if not migrant.exists() :
            migrant = models.MigrantIrregulier.objects.filter(nationalite__nom_nationalite__contains = recherche)

        if not migrant.exists() :
            migrant = models.MigrantIrregulier.objects.filter(capter_date__contains = recherche)

        if not migrant.exists() :
            migrant = models.MigrantIrregulier.objects.filter(numero_telephone__contains = recherche)

        
        return render(request,'migrant_irregulier/liste_modification.html',{'migrant':migrant})
    else :
        migrants = models.MigrantIrregulier.objects.all()
        return render(request,'migrant_irregulier/liste_modification.html',{'migrants':migrants})

