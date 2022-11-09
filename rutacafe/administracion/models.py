from distutils.command.upload import upload
from msilib.schema import Class
from random import choices
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Empredimiento(models.Model):
    CHOICE_TIPO=[
        ('hospedaje','HOSPEDAJE'),
        ('restaurante', 'RESTAURANTE'),
        ('paradas','PARADAS TURISTICAS'),

    ]
    tipo_emprendimiento: models.CharField(verbose_name="Emprendimiento",max_length=100, choices=CHOICE_TIPO)
    nombre: models.CharField(verbose_name="Emprendimiento",max_length=200)
    celular=models.CharField(verbose_name="Celular", max_length=13)
    telefono=models.CharField(verbose_name="telefono", max_length=20)
    direccion=models.CharField(verbose_name="Direccion", max_length=500)
    altitud=models.CharField(verbose_name="altitud", max_length=500) 
    latitud=models.CharField(verbose_name="latitud", max_length=500)    
    descripcion=models.TextField() 
    hora_Apertura=models.DateTimeField() 
    hora_cierre=models.DateTimeField() 
    video= models.URLField(verbose_name= "video promocional", null=True,blank=True)

    class Meta: 
        Verbose_name="Emprendimiento"
        verbose_name_plural="Emprendimientos"

    def __str__(self) -> str
        return self.tipo_emprendimiento + self.nombre_emprendimiento

    
class Persona(models.Model):
    TIPO_DOCUMENTO_CH=[
        ('cedula', 'Cedula'),
        ('pasaporte','Pasaporte'),
        
    ]
    tipo_documento= models.CharField(verbose_name="Tipo de documento", max_length=20, choices= TIPO_DOCUMENTO_CH)
    cedula=models.CharField(verbose_name="Cedula", max_length=13)
    nombres=models.CharField(verbose_name="Nombres", max_length=200)
    apellidos=models.CharField(verbose_name="Apellidos", max_length=200)
    correo_electronico=models.EmailField(verbose_name="Correo")
    celular=models.CharField(verbose_name="Celular", max_length=20)
    direccion=models.CharField(verbose_name="Direccion", max_length=500)
    fecha_nacimiento=models.DateField(verbose_name="Fecha de nacimiento")
    foto=models.ImageField(upload_to="fotos_usuarios/", verbose_name="Subir foto", null=True, blank=True)

#metodo para presentar el objeto creado
    def __str__(self):
        return self.cedula

class Clientes(Persona):
    pais_origen=models.CharField(verbose_name="Pais de Origen", max_length=200)

class Administrador(Persona):
    fecha_inicio=models.DateField()
    fecha_actualizacion=models.DateTimeField()
    estado =models.BooleanField()

class Emprendedor(Persona):
    #relacion de muchos a muchos
    emprendimientos =models.models.ManyToManyField(Emprendimiento,null=true,blank=True) 

class Meta: 
        Verbose_name="Personas que emorenden"
        verbose_name_plural="Emprendedores(personas)"


class Servicio(models.Model):
      CHOICE_TIPO=[
        ('hospedaje','HOSPEDAJE'),
        ('restaurante', 'RESTAURANTE'),
        ('paradas','PARADAS TURISTICAS'),
        ('Venta de ','PARADAS TURISTICAS'),
        ('paradas','PARADAS TURISTICAS'),












