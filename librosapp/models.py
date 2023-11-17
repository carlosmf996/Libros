from django.conf import settings
from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.TextField()
    rating = models.PositiveIntegerField()
    sinopsis = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo