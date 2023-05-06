from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length= 255, verbose_name= "Descrição")
    pontos = models.DecimalField(decimal_places = 1, max_digits = 4)
    detalhes = models.CharField(max_length= 100, blank = True, null = True)
    arquivo = models.FileField(upload_to= 'files/')

    def __str__(self):
        return "{} - {} ({})".format(self.numero, self.descricao)

class Status(models.Model):
    nome = models.CharField(max_length= 50)
    descricao = models.CharField(max_length=150, verbose_name= "Descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Classe(models.Model):
    nome = models.CharField(max_length= 50)
    nivel = models.IntegerField(verbose_name="Nível")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.nivel, self.descricao)

class Progressao(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT, verbose_name= "classe pretendida")
    data_inicial = models.DateField()
    data_final = models.DateField()
    observacao = models.CharField(max_length= 255, verbose_name= "observação")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{} -> {} | {} a {}".format(self.usuario, self.classe, self.data_inicial, self.data_final)

class Comprovante(models.Model):
    progressao = models.ForeignKey(Progressao, on_delete= models.PROTECT, verbose_name= "progressão")
    atividade = models.ForeignKey(Atividade, on_delete= models.PROTECT)
    quantidade = models.DecimalField(decimal_places= 2, max_digits= 5)
    data = models.DateField()
    data_final = models.DateField(null= True, blank= True, help_text= "Informar se o comprovante for relativo a um período.")
    arquivo = models.FileField(upload_to= 'files/')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "[{}] {} - {}/{}".format(self.pk, self.usuario, self.progressao, self.atividade)

class Comment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'pk': self.pk})


