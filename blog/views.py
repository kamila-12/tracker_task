from django.shortcuts import render
from .models import Task
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import CreateView

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'blog/task_edit.html'
    success_url = reverse_lazy('task_list')
    

class TaskDetailView(DetailView):
    model = Task 
    template_name = 'blog/task_detail.html'
    context_object_name = 'task'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_url'] = reverse('task_edit', kwargs={'pk': self.object.pk})
        return context
    
           
class TaskEditView(UpdateView):
    model = Task
    fields = ['title', 'priority_choice', 'status_choice']  # Поля, которые можно редактировать
    template_name = 'blog/task_edit.html'
    success_url = reverse_lazy('task_list')