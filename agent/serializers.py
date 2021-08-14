from rest_framework import serializers
from .models import Agent


class AgentSerializer(serializers.ModelSerializer) :
    class Meta :
        Model = Agent
        fields = '__all__'