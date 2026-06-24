from django.db import models
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    poster_at = models.DateTimeField(default=timezone.now)
    due_at = models.DateTimeField(null=True, blank=True)