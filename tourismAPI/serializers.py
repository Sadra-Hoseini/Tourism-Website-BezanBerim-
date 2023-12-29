from rest_framework import serializers
from tourism.models import Customer,Agency,Tour


class CustomerSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Customer
        fields = '__all__'




class AgencySerializer(serializers.ModelSerializer) :

    class Meta:
        model = Agency
        fields = '__all__'





class TourSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Tour
        fields = '__all__'