from django.urls import path
from .views import TaskListView, TaskDetailView, TaskEditView, TaskCreateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', TaskEditView.as_view(), name='task_edit'),  # URL для редактирования задачи
    path('task/new/', TaskCreateView.as_view(), name='task_new'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
