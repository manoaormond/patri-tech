from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.unidade.nome}"

class Bem(models.Model):
    nome = models.CharField(max_length=200)
    tombo = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True) # O campo está aqui!
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.tombo} - {self.nome}"