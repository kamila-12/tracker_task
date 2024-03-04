from django import forms
from .models import Task
class TaskForm (forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'priority_choice', 'status_choice']