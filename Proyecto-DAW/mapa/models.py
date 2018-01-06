from django.db import models

class facultad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class coordinates(models.Model):
    facultad = models.ForeignKey(facultad,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    imagenes = models.CharField(max_length=1000)

    def __str__(self):
        return "coordenadas = (" + self.latitude + ", " + self.longitude + ")"
