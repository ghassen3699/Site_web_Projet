from django import forms
from . import models


class ContactForm(forms.ModelForm) :
    class Meta :
        model = models.Contact
        fields = ('nom','adresse_mail','sujet','message')

        widgets = {
            'nom' : forms.TextInput(attrs={'class':"form-control",'placeholder':'Le nom et Le Prenom ...'}),
            'adresse_mail' : forms.EmailInput(attrs={'class':"form-control",'placeholder':'adresse e-mail ...'}),
            'sujet' : forms.TextInput(attrs={'class':"form-control",'placeholder':'le sujet de message ...'}),
            'message' : forms.TextInput(attrs={'class':"form-control",'placeholder':'le message ...'})
        }
    

