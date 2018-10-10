from django.db import models
from django.utils import timezone

Sexo = (
        ('0', 'Masculino'),
        ('1', 'Feminino'),
        )

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PeR(models.Model):
    nome = models.CharField(max_length=160)
    telefone = models.CharField(max_length=16)
    #estado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    deh_publi = models.DateTimeField(
            blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=Sexo, null=True)
    data_nasc = models.DateField()
    email = models.EmailField()
    pergunta = models.TextField()

    def pergunt(self):
        self.deh_publi = timezone.now()
        self.save()

    def __str__(self):
        return self.pergunta

