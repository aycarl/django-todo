from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # Renamed from createdAt

    class Meta:
        ordering = ['-created_at'] # Updated to use renamed field
        managed = True
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
