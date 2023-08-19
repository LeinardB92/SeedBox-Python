from rest_framework import serializers
from stationApp.models import Sensors, Actuators, Crops

class SensorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'

class ActuatorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actuators
        fields = '__all__'

class CropsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields = '__all__'

    



    