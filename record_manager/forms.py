from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'Phone': forms.TextInput(attrs={
                'pattern': r'^\+\d{1,15}$', 
                'title': 'Phone number must start with "+" and followed by the country code and digits.'
                }
            ),

        }

    
       