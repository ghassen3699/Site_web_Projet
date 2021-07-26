import django_filters
from .models import *



class OperationFilter(django_filters.FilterSet) :
    class Meta :
        model = OperationTerminer
        fields = ('nom_operation','date_operation','nombre_des_migrants','nombre_des_agents','region')






