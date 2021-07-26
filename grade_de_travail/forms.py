from django import forms
from . import models


class GradeDeTravailForm(forms.ModelForm) :
    class Meta :
        model = models.GradeDeTravail
        fields = '__all__'



