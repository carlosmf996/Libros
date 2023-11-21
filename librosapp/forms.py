from .models import Libro
from django import forms


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields =["titulo", "autor", "rating", "sinopsis"]