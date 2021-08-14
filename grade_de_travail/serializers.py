from rest_framework import serializers
from .models import GradeDeTravail



class SerialiserGrade(serializers.ModelSerializer) :
    class Meta :
        model = GradeDeTravail
        fields = '__all__'