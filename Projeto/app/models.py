from django.db import models
from cadastros.models import Atividade
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    def __str__(self):
        return self.title