from django.db import models

PRIORITY_CHOICES = (
    ('low', 'Низкий'),
    ('medium', 'Средний'),
    ('high', 'Высокий'),
)

STATUS_CHOICES = (
    ('done', 'Выполнено'),
    ('cancelled', 'Отменено'),
    ('postponed', 'Отложено'),
)

class Task(models.Model):
    title = models.CharField(max_length=255)
    priority_choice = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    status_choice = models.CharField(max_length=50, choices=STATUS_CHOICES)
