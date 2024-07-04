from django.db import models
from usuarios.models import Usuario

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, null=False)
    nome = models.TextField(null=False)

    def __str__(self):
        return self.nome

class Doacao(models.Model):
    id_doacao  = models.AutoField(primary_key=True, null=False)
    titulo = models.TextField(null= False)
    descricao = models.TextField(null=False)
    imagem = models.ImageField(upload_to='media/')
    status = models.TextField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Pedido(models.Model):
    id_pedido  = models.AutoField(primary_key=True, null=False)
    titulo = models.TextField(null= False)
    descricao = models.TextField(null=False)
    status = models.TextField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao