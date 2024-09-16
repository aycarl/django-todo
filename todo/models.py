from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']
