from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    create_data = models.DateTimeField(default=timezone.now())
    data_publicacao = models.DateTimeField(blank=True, null=True)
    
    def Publish(self):
        self.data_publicacao = timezone.now()
        self.save()
        
    def __str__(self):
        return self.titulo
