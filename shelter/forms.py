from django import forms
from .models import AdoptionRequest

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['name', 'phone', 'email', 'message', 'animal']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ваш телефон', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ваш Email', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Расскажите о себе или задайте вопрос', 'rows': 5, 'class': 'form-input'}),
        }
        