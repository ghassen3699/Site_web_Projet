from rest_framework import serializers
from .models import MigrantIrregulier, Nationalite


class Serializer_Migrant(serializers.ModelSerializer) :
    class Meta :
        model = MigrantIrregulier
        fields = '__all__'




class Serializer_Nationalite(serializers.ModelSerializer) :
    class Meta :
        model = Nationalite
        fields = '__all__'