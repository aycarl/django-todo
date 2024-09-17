from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']
        managed = True
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
