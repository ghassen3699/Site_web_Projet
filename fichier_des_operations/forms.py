from django import forms

from . import models


class FichierOperationForm(forms.ModelForm) :
    class Meta :
        model = models.Fichier_Operation
        fields = ('du','jusqu_a','operation')




