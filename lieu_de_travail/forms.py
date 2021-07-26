from django import forms
from . import models





class ProvinceForm(forms.ModelForm) :
    class Meta :
        model = models.Province
        fields = '__all__'



class RegionForm(forms.ModelForm) :
    class Meta :
        model = models.Region
        fields = '__all__'



class Commissariat_De_Police(forms.ModelForm) :
    class Meta :
        model = models.Commissariat_De_Police
        fields = '__all__'




class Lieu_De_TravailForm(forms.ModelForm) :
    class Meta :
        model = models.Lieu_De_Travail
        fields = '__all__'


