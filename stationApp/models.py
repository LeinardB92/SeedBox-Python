from django.db import models

# Create your models here.
class Sensors(models.Model):
    id = models.IntegerField(primary_key=True)
    # Nombre compuesto según las carácteristicas del cada sensor,
    # características físicas y de ubicación.
    idSensor = models.CharField(max_length=50)
    typeOfSensor = models.CharField(max_length=20)  
    sensorNumber = models.IntegerField()  
    location = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    value = models.DecimalField(max_digits=4, decimal_places=2)
    #crops = models.OneToOneField(Crops,on_delete=models.CASCADE)
    dateOfTest = models.DateField()
    description = models.TextField() 

    def __str__(self):
        return self.idSensor


class Actuators(models.Model):
    id = models.IntegerField(primary_key=True)
    idActuator = models.CharField(max_length=50)
    typeOfActuator = models.CharField(max_length=20)
    actuatorNumber = models.IntegerField()
    location = models.CharField(max_length=20)
    state =  models.CharField(max_length=15)
    value = models.DecimalField(max_digits=4, decimal_places=2)
    #crops = models.OneToOneField(Crops,on_delete=models.CASCADE)
    dateOfTest = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.idActuator
    

class Crops(models.Model):
    id = models.IntegerField(primary_key=True)
    idCrop = models.CharField(max_length=50)
    typeOfCrop = models.CharField(max_length=20)
    CropNumber = models.IntegerField()
    location = models.CharField(max_length=20)
    stage =  models.CharField(max_length=15)
    sensors = models.OneToOneField(Sensors,on_delete=models.CASCADE)
    actuators = models.OneToOneField(Actuators,on_delete=models.CASCADE)
    plantingDate = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.idCrop