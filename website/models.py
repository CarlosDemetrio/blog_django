from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    resumo = RichTextField(default=1)
    conteudo = RichTextUploadingField()
    create_data = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField(blank=True, null=True)
    
    def Publish(self):
        self.data_publicacao = timezone.now()
        self.save()
        
    def __str__(self):
        return self.titulo
