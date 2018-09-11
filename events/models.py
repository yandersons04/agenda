from django.db import models

class Event(models.Modek):

    priorities_list = (
        ('0', 'Sem Prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente'),
        ('4', 'Ultra mega hiper Urgente'),
    )

    date = models.DateField()
    event = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=priorities_list)

    def __str__ (self):
        return self.event
