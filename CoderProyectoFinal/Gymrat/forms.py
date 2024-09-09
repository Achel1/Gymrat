from django import forms
from django.contrib.auth.models import User
from .models import Miembro


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class MiembroEditForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ["avatar"]
