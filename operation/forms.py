from django import forms
from . import models



class OperationTerminerForm(forms.ModelForm) :
    class Meta :
        model = models.OperationTerminer
        fields = ('nom_operation','date_operation','agent_fk','nombre_des_agents','nombre_des_migrants','region','province','commissariat')


