from django import forms

from apps.pages.models import Service, Team


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name',
            'description',
        ]


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'occupation',
            ]