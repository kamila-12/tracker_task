from django.urls import path
from .views import TaskListView, TaskDetailView, TaskEditView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', TaskEditView.as_view(), name='task_edit'),  # URL для редактирования задачи
]
