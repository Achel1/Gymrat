from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from Gymrat.models import Entrenador, Asistencia, Plan, Clase
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from Gymrat.mixins import SuperuserRequiredMixin


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Gymrat.forms import UserEditForm, MiembroEditForm
from .models import Miembro


@login_required
def editar_usuario(request):
    user = request.user
    miembro, created = Miembro.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=user)
        miembro_form = MiembroEditForm(request.POST, request.FILES, instance=miembro)

        if user_form.is_valid() and miembro_form.is_valid():
            user_form.save()
            miembro_form.save()
            return redirect("inicio")  # Redirige a la URL nombrada 'inicio'
    else:
        user_form = UserEditForm(instance=user)
        miembro_form = MiembroEditForm(instance=miembro)

    return render(
        request,
        "editar_usuario.html",
        {"user_form": user_form, "miembro_form": miembro_form},
    )


def no_autorizado(request):
    return render(request, "no_autorizado.html")


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registro.html"
    success_url = reverse_lazy("inicio")


class CustomLogoutView(LogoutView):
    template_name = "logout.html"

    def get_success_url(self):
        return reverse_lazy("inicio")


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("inicio")


def inicio(request):
    return render(request, "index.html")


# Aqui comienza clase
class ClaseListView(LoginRequiredMixin, ListView):
    model = Clase
    template_name = "clase.html"
    login_url = "login"  #


class ClaseDetailView(LoginRequiredMixin, DetailView):
    model = Clase
    template_name = "clase_detalle.html"
    login_url = "login"


class ClaseDelete(LoginRequiredMixin, DeleteView):
    model = Clase
    template_name = "clase_eliminar.html"
    success_url = reverse_lazy("ListaClase")
    login_url = "login"


class ClaseCreateView(LoginRequiredMixin, CreateView):
    model = Clase
    template_name = "clase_crear.html"
    success_url = reverse_lazy("ListaClase")
    fields = ["nombre", "descripcion", "horario"]
    login_url = "login"


class ClaseUpdate(LoginRequiredMixin, UpdateView):
    model = Clase
    template_name = "clase_actualizar.html"
    success_url = reverse_lazy("ListaClase")
    fields = ["nombre", "descripcion", "horario"]
    login_url = "login"


# Aqui comienza plan


class PlanListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = "plan.html"
    login_url = "login"  # Redirige a esta URL si el usuario no está autenticado


class PlanDetailView(LoginRequiredMixin, DetailView):
    model = Plan
    template_name = "plan_detalle.html"
    login_url = "login"


class PlanDelete(LoginRequiredMixin, DeleteView):
    model = Plan
    template_name = "plan_eliminar.html"
    success_url = reverse_lazy("ListaPlan")
    login_url = "login"


class PlanCreateView(LoginRequiredMixin, CreateView):
    model = Plan
    template_name = "plan_crear.html"
    success_url = reverse_lazy("ListaPlan")
    fields = ["nombre", "descripcion", "duracion"]
    login_url = "login"


class PlanUpdate(LoginRequiredMixin, UpdateView):
    model = Plan
    template_name = "plan_actualizar.html"
    success_url = reverse_lazy("ListaPlan")
    fields = ["nombre", "descripcion", "duracion"]
    login_url = "login"


# Aqui comienza Asistensia


class AsistenciaListView(LoginRequiredMixin, ListView):
    model = Asistencia
    template_name = "asistencia.html"
    login_url = "login"


class AsistenciaDetailView(LoginRequiredMixin, DetailView):
    model = Asistencia
    template_name = "asistencia_detalle.html"
    fields = ["miembro", "clase", "fecha"]
    login_url = "login"


class AsistenciaCreatView(LoginRequiredMixin, CreateView):
    model = Asistencia
    template_name = "asistencia_crear.html"
    success_url = reverse_lazy("ListaAsistencia")
    fields = ["miembro", "clase", "fecha"]
    login_url = "login"


class AsistenciaUpdate(LoginRequiredMixin, UpdateView):
    model = Asistencia
    template_name = "asistencia_actualizar.html"
    success_url = reverse_lazy("ListaAsistencia")
    fields = ["miembro", "clase", "fecha"]
    login_url = "login"


class AsistenciaDelete(LoginRequiredMixin, DeleteView):
    model = Asistencia
    template_name = "asistencia_eliminar.html"
    success_url = reverse_lazy("ListaAsistencia")
    login_url = "login"


# Comienza Entrenador


class EntrenadorListView(LoginRequiredMixin, ListView):
    model = Entrenador
    template_name = "entrenador.html"
    login_url = "login"


class EntrenadorDetailView(LoginRequiredMixin, DetailView):
    model = Entrenador
    template_name = "entrenador_detalle.html"
    login_url = "login"


class EntrenadorCreatView(SuperuserRequiredMixin, LoginRequiredMixin, CreateView):
    model = Entrenador
    template_name = "entrenador_crear.html"
    success_url = reverse_lazy("ListaEntrenador")
    fields = ["nombre", "especialidad", "experiencia"]
    login_url = "login"


class EntrenadorUpdate(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Entrenador
    template_name = "entrenador_actualizar.html"
    success_url = reverse_lazy("ListaEntrenador")
    fields = ["nombre", "especialidad", "experiencia"]
    login_url = "login"


class EntrenadorDeleteview(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Entrenador
    template_name = "entrenador_eliminar.html"
    success_url = reverse_lazy("ListaEntrenador")
    login_url = "login"
