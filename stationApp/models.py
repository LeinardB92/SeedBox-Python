from datetime import date
from django.db import models

# Create your models here.
class Sensors(models.Model):
    """Datos que NO deben de ser llenados obligatoriamente por el usuario"""
    # Numeración automática para cadauno de 
    id = models.AutoField(primary_key=True)
    # Nombre compuesto según las carácteristicas físicas y ubicación del dispositivo.
    idSensor = models.CharField(max_length=70, unique=True, editable=False)
    # Debe obtener un valor automático dependiendode del número de ejemplaresde un 
    # mismo tipo de sensor.
    sensorNumber = models.IntegerField(editable=False)  
    # Obtiene su valor del estado en el que se encuentre el sensor Activated o
    # Desactivated
    state = models.CharField(max_length=15)
    # Campo requerido unicamente para sensores que no sean de dos estados.
    value = models.DecimalField(max_digits=10, decimal_places=2)
    # Obtiene su valor de la fecha de instalación del dispositivo.
    installationDate = models.DateField(default=date.today)
    
    """Datos que deben de ser llenados obligatoriamente por el usuario"""
    typeOfSensor = models.CharField(max_length=20)  
    location = models.CharField(max_length=20)
    #crops = models.OneToOneField(Crops,on_delete=models.CASCADE)
    description = models.TextField() 

    # Construir el valor para ´idSensor´.
    def save(self, *args, **kwargs):        
        # Una forma de leer el comportamiento de este filtro: Traeme los valores del campo ´self.typeOfSensor´ de la base de datos que coincidan con el valor del campo ´typeOfSensor´ del objeto en el que estamos trabajando actualmente. Postgeriormente se contabilizan estos resultados y se guardan. 
        repetitions = Sensors.objects.filter(typeOfSensor=self.typeOfSensor).count()
        # Asignar el número de repeticiones al campo sensorNumber
        
        self.sensorNumber = repetitions + 1
        self.idSensor = f"{self.sensorNumber}-{self.typeOfSensor}-{self.location}"

        super(Sensors, self).save(*args, **kwargs)


    def __str__(self):
        return self.idSensor



class Actuators(models.Model):
    id = models.AutoField(primary_key=True)
    idActuator = models.CharField(max_length=50)
    typeOfActuator = models.CharField(max_length=20)
    actuatorNumber = models.IntegerField()
    location = models.CharField(max_length=20)
    state =  models.CharField(max_length=15)
    value = models.DecimalField(max_digits=4, decimal_places=2)
    #crops = models.OneToOneField(Crops,on_delete=models.CASCADE)
    installationDate = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.idActuator
    


class Crops(models.Model):
    id = models.AutoField(primary_key=True)
    idCrop = models.CharField(max_length=50)
    typeOfCrop = models.CharField(max_length=20)
    CropNumber = models.IntegerField()
    location = models.CharField(max_length=20)
    stage =  models.CharField(max_length=15)
    # sensors = models.ForeignKey(Sensors,on_delete=models.CASCADE, default=0)
    # actuators = models.ForeignKey(Actuators,on_delete=models.CASCADE, default=0)
    plantingDate = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.idCrop