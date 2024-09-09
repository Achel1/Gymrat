from django.http import HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin


class SuperuserRequiredMixin(AccessMixin):
    """Mixin que requiere que el usuario sea un superusuario."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        # Redirigir a una página de error personalizada o devolver una respuesta con un mensaje específico
        return redirect(reverse("no_autorizado"))  # 'no_autorizado'
