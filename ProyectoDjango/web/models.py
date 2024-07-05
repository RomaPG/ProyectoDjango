from django.db import models

# Create your models here.
class Usuario(models.Model):
    gmail = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    nombre = models.CharField(primary_key=True,max_length=20)
    apellido = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)  # Considera usar un campo de contraseña seguro en producción
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
