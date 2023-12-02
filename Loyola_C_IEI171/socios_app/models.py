from django.db import models

ESTADOS_SELECT = [
    ('V', 'Vigente'),
    ('S', 'Suspendido'),
    ('R', 'Retirado'),
]

SEXO_SELECT = [
    ('F', 'Femenino'),
    ('M', 'Masculino'),
    ('O', '39 tipos de gay'),
]

class Socios(models.Model):
    nombreSocio=models.CharField(max_length=80)
    fechaIncorporacion=models.DateField()
    anoNacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    sexo = models.CharField(max_length=1, choices=SEXO_SELECT)
    estado = models.CharField(max_length=1, choices=ESTADOS_SELECT)
    observacion = models.TextField(blank=True, null=True)