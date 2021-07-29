from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import redirect, render
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from . import filters


@login_required(login_url='login')
def ajouter_migrant(request) :
    form = forms.MigrantIrregulierForm()
    if request.method == 'POST' :
        form = forms.MigrantIrregulierForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('ajouter_migrant')
        else :
            return render(request,'migrant_irregulier/ajouter_migrant.html',{'form':form})
    return render(request,'migrant_irregulier/ajouter_migrant.html',{'form':form})



@login_required(login_url='login')
def home(request) :
    migrants = models.MigrantIrregulier.objects.all()
    filter = filters.MigrantFilter(request.GET,queryset=migrants)
    migrants = filter.qs
    prenom_agent = request.user.agent.prenom
    nom_agent = request.user.agent.nom
    return render(request,'migrant_irregulier/home.html',{'migrants':migrants ,
                                                           'agent_nom':nom_agent,
                                                           'filter':filter,
                                                           'agent_prenom':prenom_agent})





@login_required(login_url='login')
def modifier_migrant(request,pk) :
    migrant = models.MigrantIrregulier.objects.get(id = pk)
    form = forms.MigrantIrregulierForm(instance=migrant)

    if request.method == 'POST' :
        form = forms.MigrantIrregulierForm(request.POST ,instance=migrant)
        if form.is_valid() :
            form.save()
            return redirect('page_home_migrant')
        else :
            return render(request,'migrant_irregulier/ajouter_migrant.html',{'form':form})
    return render(request,'migrant_irregulier/ajouter_migrant.html',{'form':form})




@login_required(login_url='login')
def supprimer_migrant(request,pk) :
    migrant = models.MigrantIrregulier.objects.get(id=pk)

    if request.method == 'POST' :
        migrant.delete()
        return redirect('page_home_migrant')
    return render(request,'migrant_irregulier/supprimer_migrant.html',{'migrant':migrant})




def export_fichier_csv(request) :

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)

    writer.writerow(['nom','prenom','age','n°cin','n°passport','sexe','n°telephone','nationalite','operation','capter_date'])


    for Migrant in models.MigrantIrregulier.objects.all().values_list('nom','prenom','age','numero_cin','numero_passport','sexe','numero_telephone','nationalite','operation','capter_date') :
        writer.writerow(Migrant)

    response['Content-Disposition'] = 'attachement; filename = "fichier des migrants.csv" '

    return response




