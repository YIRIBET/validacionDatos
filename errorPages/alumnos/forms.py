from django import forms
from .models import Alumnos

class AlumnoForm(forms.ModelForm):
    # Campo oculto para el ID del alumno
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']  # Campos que deseas mostrar en el formulario

    def clean(self):
        cleaned_data = super().clean()
        # Aquí puedes realizar validaciones adicionales si es necesario
        return cleaned_data
