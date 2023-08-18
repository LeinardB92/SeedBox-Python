from django.shortcuts import render
from stationApp.models import *
from stationApp.serializers import *
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.

class SensorsViewSet(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializers

class ActuatorsViewSet(viewsets.ModelViewSet):
    queryset = Actuators.objects.all()
    serializer_class = ActuatorsSerializers

class CropsViewSet(viewsets.ModelViewSet):
    queryset = Crops.objects.all()
    serializer_class = CropsSerializers

    

