from fichier_des_operations.serializers import serializers_Fichier
from django.shortcuts import redirect, render
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from . import filters



from rest_framework.decorators import api_view
from rest_framework.response import Response






@login_required(login_url='login')
def home(request) :
    return render(request,'fichier_des_operations/home.html')





@login_required(login_url='login')
def creer_fichier_operation_view(request) :
    
    form = forms.FichierOperationForm()
    if request.method == 'POST' :
        form = forms.FichierOperationForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('creer_fichier')
        else :
            return render(request,'fichier_des_operations/fichier_operation.html',{'form':form})
    return render(request,'fichier_des_operations/fichier_operation.html',{'form':form})




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




@api_view(['GET'])
def fichier_api(request) :
    les_fichiers = models.Fichier_Operation.objects.all()
    fichier_ser = serializers_Fichier(les_fichiers, many=True)

    return Response(fichier_ser.data)