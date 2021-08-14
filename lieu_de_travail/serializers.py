from rest_framework import serializers
from .models import Lieu_De_Travail,Province,Region,Commissariat_De_Police


class Serializer_LieuDeTravail(serializers.ModelSerializer) :
    class Meta :
        model = Lieu_De_Travail
        fields = '__all__'


class SerializerProvince(serializers.ModelSerializer) :
    class Meta :
        model = Province
        fields = '__all__'


class SerializeRegion(serializers.ModelSerializer) :
    class Meta :
        model = Region
        fields = '__all__'



class SerializeCommissariat(serializers.ModelSerializer) :
    class Meta : 
        model = Commissariat_De_Police
        fields = '__all__' 
