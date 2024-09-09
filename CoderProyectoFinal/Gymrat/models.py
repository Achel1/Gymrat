from django.db import models
from django.contrib.auth.models import User


class Miembro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    avatar = models.ImageField(upload_to="avatares/", blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    experiencia = models.TextField()

    def __str__(self):
        return self.nombre


from django.utils import timezone


class Asistencia(models.Model):
    miembro = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )  # Cambia 'auth.User' si usas otro modelo de usuario
    fecha = models.DateField(default=timezone.now)
    clase = models.ForeignKey(
        "Clase", on_delete=models.CASCADE
    )  # Asume que tienes un modelo 'Clase'

    def __str__(self):
        return f"{self.miembro} - {self.clase} - {self.fecha}"


class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField()  # Duración en días

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    horario = models.TimeField()

    def __str__(self):
        return self.nombre


# Modelo Entrenador:
# Define el nombre, especialidad y experiencia del entrenador.

# Modelo Asistencia:
# Registra qué miembro asistió a qué clase y en qué fecha.

# Modelo Plan:
# Define los planes de entrenamiento con nombre, descripción y duración.


# Modelo Clase:
# Define las clases o sesiones de entrenamiento, incluyendo nombre, descripción y horario.
