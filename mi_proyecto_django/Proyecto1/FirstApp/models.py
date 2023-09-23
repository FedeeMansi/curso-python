from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=50, null=False, default='')
    peso = models.IntegerField(null=False, default=0)  # Aquí establecemos un valor predeterminado de 0

class Credenciales_P(models.Model):
    nombre = models.CharField(max_length=50, null=False, default='')
    apellido = models.CharField(max_length=50, null=False, default='')
    email = models.CharField(max_length=50, null=False, default='user123@hotmail.com')
    password = models.CharField(max_length=50, null=False, default='')
    
    def __str__(self):
         return f'{self.nombre}, {self.apellido}'

class Credenciales_DB(models.Model):
    host = models.CharField(max_length=150, null=False, default='user123@hotmail.com')
    port =  models.IntegerField(max_length=4, null=False, default=5432)
    usuario = models.CharField(max_length=50, null=False, default='')
    password = models.CharField(max_length=50, null=False, default='')
    db_name = models.CharField(max_length=50, null=False, default='postgres')# Puedes establecer el valor predeterminado como una cadena vacía ('')


class random_pwd(models.Model):
    password = models.CharField(max_length=50, null=False, default='a35hfgssrDa4tasda2')  # 
    
class Contactarnos(models.Model):
        nombre = models.CharField(max_length=50, null=False, default='')
        email = models.CharField(max_length=50, null=False, default='user123@hotmail.com')
        numero = models.IntegerField(null=False, default=0)
        mensaje = models.CharField(max_length=400, null=False, default='')
        
        def __str__(self):
            return f'{self.nombre}, {self.email}'
        

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name