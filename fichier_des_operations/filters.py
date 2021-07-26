import django_filters


from .models import *

class FichierFilter(django_filters.FilterSet) :
    class Meta :
        model = Fichier_Operation
        fields = ('du','jusqu_a','operation')




