from rest_framework.decorators import api_view
from rest_framework.response import Response
from migrant_irregulier.serializers import Serializer_Migrant
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from . import models
from . import forms
from django.contrib.auth.decorators import login_required

from . import filters




'''
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
'''





'''
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
'''


'''
@login_required(login_url='login')
def supprimer_migrant(request,pk) :
    migrant = models.MigrantIrregulier.objects.get(id=pk)

    if request.method == 'POST' :
        migrant.delete()
        return redirect('page_home_migrant')
    return render(request,'migrant_irregulier/supprimer_migrant.html',{'migrant':migrant})

'''

@api_view(['GET'])
@login_required(login_url='login')
def migrant_irregulier_api(request) :
    les_migrants = models.MigrantIrregulier.objects.all()

    les_migrants_ser = Serializer_Migrant(les_migrants, many = True)

    return Response(les_migrants_ser.data)





@login_required(login_url='login')
def home(request) :
    return render(request,'migrant_irregulier/home.html')


