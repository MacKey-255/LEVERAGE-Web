from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from system.validators import file_size


class Restore(forms.ModelForm):
    username = forms.CharField(
        label=_("Username"),
    )
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class SkinsForm(forms.Form):
    upload = forms.ImageField(
        label="Skins",
        validators=[file_size],
        required=True
    )
