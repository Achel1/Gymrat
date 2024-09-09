from django.contrib import admin


from django.contrib import admin
from .models import Entrenador, Asistencia, Plan, Clase


from django.contrib import admin


@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especialidad", "experiencia")


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("miembro", "fecha", "clase")


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "duracion")


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "horario")
