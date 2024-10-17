from django.db import models

# Create your models here.
class Eleitor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    secao = models.CharField(max_length=10)
    zona = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.nome