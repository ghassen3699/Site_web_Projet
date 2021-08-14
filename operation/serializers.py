from rest_framework import serializers
from .models import OperationTerminer



class OperationSerializer(serializers.ModelSerializer) :
    class Meta :
        model = OperationTerminer
        fields = '__all__'



