from django import forms
from .models import Issues, Donations


class IssuesForm(forms.ModelForm):
    class Meta:
        model = Issues
        exclude = ('accept', 'creationDate', 'wroteBy')


class DonationsForm(forms.ModelForm):
    class Meta:
        model = Donations
        exclude = ('accepted', 'owner', 'creationDate')