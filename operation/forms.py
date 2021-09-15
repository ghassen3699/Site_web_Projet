from django import forms
from . import models



class OperationTerminerForm(forms.ModelForm) :
    class Meta :
        model = models.OperationTerminer
        fields = ('nom_operation','date_operation','nature_operation','les_migrants','nombre_des_migrants','nombre_des_agents','region','province')

        widgets = {
            'nom_operation' : forms.TextInput(attrs={'class':"form-control",'placeholder':"Le nom de l'operation..."}),
            'date_operation' : forms.DateInput(attrs={'class':"form-control",'placeholder':"JJ-MM-AAAA"}),
            'nombre_des_migrants' : forms.NumberInput(attrs={'class':"form-control",'placeholder':'nombre des migrants ...'}),
            'nombre_des_agents' : forms.NumberInput(attrs={'class':"form-control",'placeholder':'nombre des agents ...'}),
            'region' : forms.Select(attrs={'class':"form-select",'placeholder':'LA Region  ...'}),
            'nature_operation' : forms.Select(attrs={'class':"form-select",'placeholder':"LA Nature De L'operation  ..."}),
            'province' : forms.Select(attrs={'class':"form-select",'placeholder':'La Province ...'}),
            'les_migrants' : forms.SelectMultiple(attrs={'class':"form-select",'placeholder':'Les Migrants  ...'}),
        }


