from django.db import models

# Create your models here.


class Productos(models.Model):
    nombre: models.CharField(max_length=50)
    peso: models.IntegerField()
    
class Credenciales(models.Model):
    usuario: models.CharField(max_length=50)
    password: models.CharField(max_length=50)