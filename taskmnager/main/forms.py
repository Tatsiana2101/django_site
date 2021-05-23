from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "price"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваше имя'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Оставьте отзыв'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оцените нас от 1 до 5  :) '
            }),
        }