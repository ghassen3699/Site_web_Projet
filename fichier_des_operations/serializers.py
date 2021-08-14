from rest_framework import serializers
from .models import Fichier_Operation


class serializers_Fichier(serializers.ModelSerializer) :
    class Meta :
        model = Fichier_Operation
        fields = '__all__'