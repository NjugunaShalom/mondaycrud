from django import forms

from patient.models import Patient, Diagnosis, Doctor


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control',
                       'accept': 'image/*',
                       'title':'Select an Image'}
            ),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter your email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Enter your age'}),
            'gender': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your gender'}),
        }