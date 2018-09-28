from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 200)
    texto = models.TextField()
    data_criado = models.DateField (default = timezone.now)
    data_publi = models.DateTimeField (blank = True, null = True)

    def publish(self):
        self.data_publi = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
