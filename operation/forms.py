from django import forms
from . import models



class OperationTerminerForm(forms.ModelForm) :
    class Meta :
        model = models.OperationTerminer
        fields = ('nom_operation','date_operation','nature_operation','les_migrants','nombre_des_migrants','region','province','commissariat')

        widgets = {
            'nom_operation' : forms.TextInput(attrs={'class':"form-control",'placeholder':"Le nom de l'operation..."}),
            'date_operation' : forms.DateInput(attrs={'class':"form-control",'placeholder':"La Date de l'operation..."}),
            'nombre_des_migrants' : forms.NumberInput(attrs={'class':"form-control",'placeholder':'nombre des migrants ...'}),
            'region' : forms.Select(attrs={'class':"form-select",'placeholder':'LA Region  ...'}),
            'province' : forms.Select(attrs={'class':"form-select",'placeholder':'La Province ...'}),
            'commissariat' : forms.Select(attrs={'class':"form-select",'placeholder':'Le Commissariat ...'}),
            'les_migrants' : forms.SelectMultiple(attrs={'class':"form-select",'placeholder':'Les Migrants  ...'}),
        }


