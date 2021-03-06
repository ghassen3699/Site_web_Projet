from django import forms
from . import models


class AgentForm(forms.ModelForm) :
    class Meta :
        model = models.Agent
        fields = ('nom','prenom','age','genre','numero_telephone','grade_de_travail_fk','numero_cin','adresse','code_postal')


        widgets = {
            'nom' : forms.TextInput(attrs={'class':'form-control','placeholder':"Le Nom ..."}),
            'prenom' : forms.TextInput(attrs={'class':'form-control','placeholder':"Le Prenom ..."}),
            'age' : forms.NumberInput(attrs={'class':'form-control','placeholder':"L'age ..."}),
            'genre' : forms.Select(attrs={'class':"form-select",'placeholder':""}),
            'numero_telephone': forms.TextInput(attrs={'class':'form-control','placeholder':"Le Numero Telephone ..."}),
            'grade_de_travail_fk': forms.Select(attrs={'class':"form-select",'placeholder':"Le Grade De Travail..."}),
            'numero_cin' : forms.TextInput(attrs={'class':'form-control','placeholder':"CIN ..."}),
            'adresse' : forms.TextInput(attrs={'class':'form-control','placeholder':"L'adresse ..."}),
            'code_postal' : forms.TextInput(attrs={'class':'form-control','placeholder':"Le Code Postal ..."}),
        }




