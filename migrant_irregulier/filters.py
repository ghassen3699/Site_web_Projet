import django_filters



from .models import *

class MigrantFilter(django_filters.FilterSet) :
    class Meta :
        model = MigrantIrregulier
        fields = ('numero_cin','numero_passport','nom','prenom','nationalite')



