from django import forms
from system.validators import json_validator


class JsonForm(forms.Form):
    json = forms.CharField(validators=[json_validator])
    type = forms.CharField(max_length=16, widget=forms.HiddenInput)
