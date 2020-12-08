from rest_framework import serializers
from .models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    Ptype = serializers.CharField(required = False) 
    Psize = serializers.CharField(required = False)
    Ptop = serializers.CharField(required = False)
    class Meta:
        model = Pizza
        #fields = {'Ptype','Psize','Ptop'}
        fields = '__all__'
