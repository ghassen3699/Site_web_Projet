from django import forms
from . import models


class MigrantIrregulierForm(forms.ModelForm) :
    class Meta :
        model = models.MigrantIrregulier
        fields = ('nom','prenom','age','numero_cin','copie_cin','numero_passport','copie_passport','sexe','numero_telephone','photo_personnel','nationalite','capter_date','description')


        widgets = {
            'nom' : forms.TextInput(attrs={'class':"form-control",'placeholder':"Le nom ..."}),
            'prenom' : forms.TextInput(attrs={'class':"form-control",'placeholder':"Le prenom ..."}),
            'numero_cin' : forms.TextInput(attrs={'class':"form-control",'placeholder':"numero CIN ..."}),
            'numero_passport' : forms.TextInput(attrs={'class':"form-control",'placeholder':"Numero passport ..."}),
            'numero_telephone' : forms.TextInput(attrs={'class':"form-control",'placeholder':"Numero telephone ..."}),
            'capter_date' : forms.DateInput(attrs={'class':"form-control",'placeholder':"La Date de capte..."}),
            'age' : forms.NumberInput(attrs={'class':"form-control",'placeholder':"age ..."}),
            'nationalite' : forms.Select(attrs={'class':"form-select",'placeholder':'La nationalite  ...'}),
            'sexe' : forms.Select(attrs={'class':"form-select",'placeholder':'Le genre ...'}),
            'description' : forms.TextInput(attrs={'class':"form-control",'placeholder':"Une description ..."}),
            'photo_personnel' : forms.FileInput(attrs={'class':"form-control",'placeholder':"Une description ..."}),
            'copie_cin' : forms.FileInput(attrs={'class':"form-control",'placeholder':"Une description ..."}),
            'copie_passport' : forms.FileInput(attrs={'class':"form-control",'placeholder':"Une description ..."})


        }






