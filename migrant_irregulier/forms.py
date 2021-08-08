from django import forms
from . import models


class MigrantIrregulierForm(forms.ModelForm) :
    class Meta :
        model = models.MigrantIrregulier
        fields = ('nom','prenom','age','numero_cin','copie_cin','numero_passport','copie_passport','sexe','numero_telephone','photo_personnel','nationalite','capter_date','description')






