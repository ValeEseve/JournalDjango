# forms.py
from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'mood',
            'title',
            'content',
            'weather_icon',
            'temperature',
            'location',
            'latitude',
            'longitude',
        ]
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la entrada'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu entrada aquí...', 'rows': 4}),
            'weather_icon': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
        }
