from django import forms
from . import models


class AgentForm(forms.ModelForm) :
    class Meta :
        model = models.Agent
        fields = ('nom','prenom','age','sexe','numero_telephone','grade_de_travail_fk','lieu_de_travail_fk','numero_cin','copie_cin')




