from django import forms
from . import models


class AgentForm(forms.ModelForm) :
    class Meta :
        model = models.Agent
        fields = ('nom','prenom','age','sexe','numero_telephone','grade_de_travail_fk','lieu_de_travail_fk','numero_cin','copie_cin','adresse','code_postal')


        widgets = {
            'nom' : forms.TextInput(attrs={'class':'form-control','placeholder':"Le Nom De L'agent"}),
            'prenom' : forms.TextInput(attrs={'class':'form-control','placeholder':"Le Prenom De L'agent"}),
            'age' : forms.NumberInput(attrs={'class':'form-control','placeholder':"L'age De L'agent"}),
            'sexe' : forms.Select(attrs={'class':"form-select",'placeholder':"Le Sexe De L'agent..."}),
            'numero_telephone': forms.TextInput(attrs={'class':'form-control','placeholder':"Le Numero Telephone De L'agent"}),
            'grade_de_travail_fk': forms.Select(attrs={'class':"form-select",'placeholder':"Le Grade De Travail..."}),
            'lieu_de_travail_fk' : forms.Select(attrs={'class':"form-select",'placeholder':"Le Lieu De Travail..."}),
            'numero_cin' : forms.TextInput(attrs={'class':'form-control','placeholder':"Le Numero CIN"}),
            'copie_cin' : forms.FileInput(attrs={'class':"form-select",'placeholder':"Une Copie CIN..."}) ,
            'adresse' : forms.TextInput(attrs={'class':'form-control','placeholder':"L'adresse De L'agent"}),
            'code_postal' : forms.TextInput(attrs={'class':'form-control','placeholder':"Le Code Postal De L'adresse De L'agent"}),
        }




