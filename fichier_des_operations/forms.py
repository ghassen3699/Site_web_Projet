from django import forms
from . import models


class FichierOperationForm(forms.ModelForm) :
    class Meta :
        model = models.Fichier_Operation
        fields = ('du','jusqu_a','operation')
    
        widgets = {
            'du': forms.DateInput(attrs={'class':'form-control','placeholder':"La Date Du Debut Du Fichier..."}) ,
            'jusqu_a': forms.DateInput(attrs={'class':'form-control','placeholder':"La Date Final Du Fichier..."}) ,
            'operation': forms.SelectMultiple(attrs={'class':"form-select",'placeholder':'Les Operations  ...'}),
        }




