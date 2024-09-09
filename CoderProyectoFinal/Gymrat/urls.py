from django.urls import path
from . import views
from Gymrat.views import (
    EntrenadorListView,
    EntrenadorDetailView,
    EntrenadorCreatView,
    EntrenadorUpdate,
    EntrenadorDeleteview,
    AsistenciaListView,
    AsistenciaDetailView,
    AsistenciaCreatView,
    AsistenciaUpdate,
    AsistenciaDelete,
    PlanListView,
    PlanDetailView,
    PlanCreateView,
    PlanUpdate,
    PlanDelete,
    ClaseListView,
    ClaseDetailView,
    ClaseCreateView,
    ClaseUpdate,
    ClaseDelete,
)
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login
from Gymrat.views import no_autorizado
from .views import editar_usuario

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("entrenador/", EntrenadorListView.as_view(), name="Entrenador"),
    path("entrenador/lista", EntrenadorListView.as_view(), name="ListaEntrenador"),
    path(
        "entrenador/<int:pk>/", EntrenadorDetailView.as_view(), name="DetalleEntrenador"
    ),
    path("entrenador/nuevo/", EntrenadorCreatView.as_view(), name="CrearEntrenador"),
    path(
        "entrenador/<int:pk>/editar/",
        EntrenadorUpdate.as_view(),
        name="ActualizarEntrenador",
    ),
    path(
        "entrenador/<int:pk>/eliminar/",
        EntrenadorDeleteview.as_view(),
        name="EliminarEntrenador",
    ),
    path("asistencia/", AsistenciaListView.as_view(), name="ListaAsistencia"),
    path(
        "asistencia/<int:pk>/", AsistenciaDetailView.as_view(), name="DetalleAsistencia"
    ),
    path("asistencia/crear/", AsistenciaCreatView.as_view(), name="CrearAsistencia"),
    path(
        "asistencia/<int:pk>/editar/",
        AsistenciaUpdate.as_view(),
        name="ActualizarAsistencia",
    ),
    path(
        "asistencia/<int:pk>/eliminar/",
        AsistenciaDelete.as_view(),
        name="EliminarAsistencia",
    ),
    path("plan/", PlanListView.as_view(), name="ListaPlan"),
    path("plan/<int:pk>/", PlanDetailView.as_view(), name="DetallePlan"),
    path("plan/crear/", PlanCreateView.as_view(), name="CrearPlan"),
    path("plan/<int:pk>/editar/", PlanUpdate.as_view(), name="ActualizarPlan"),
    path("plan/<int:pk>/eliminar/", PlanDelete.as_view(), name="EliminarPlan"),
    path("clase/", ClaseListView.as_view(), name="ListaClase"),
    path("clase/<int:pk>/", ClaseDetailView.as_view(), name="DetalleClase"),
    path("clase/crear/", ClaseCreateView.as_view(), name="CrearClase"),
    path("clase/<int:pk>/editar/", ClaseUpdate.as_view(), name="ActualizarClase"),
    path("clase/<int:pk>/eliminar/", ClaseDelete.as_view(), name="EliminarClase"),
    # Ruta para el inicio de sesión
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registro/", views.RegisterView.as_view(), name="registro"),
    path("logout/", logout_then_login, {"login_url": "index"}, name="logout"),
    path("no-autorizado/", no_autorizado, name="no_autorizado"),
    path("editar_usuario/", editar_usuario, name="editar_usuario"),
    # Otras rutas...
]
