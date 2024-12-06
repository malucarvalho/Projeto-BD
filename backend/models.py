from django.db import models
from django.utils.timezone import now

class Editora(models.Model):
    editora = models.CharField(max_length=50)
    local = models.CharField(max_length=50, default='Brasil')

    def __str__(self):
        return self.editora
    
class Autor(models.Model):
    nome = models.CharField(max_length=50)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50, default='Desconhecido')
    ano = models.IntegerField(default=2024)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_usuario

class Reserva(models.Model):
    reserva_id = models.IntegerField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_reserva = models.DateField(default=now)

    def __str__(self):
        return f'{self.reserva_id} - {self.livro} - {self.usuario}'

class Emprestimo(models.Model):
    emprestimo_id = models.IntegerField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(default=now)

    def __str__(self):
        return f'{self.emprestimo_id} - {self.livro} - {self.usuario}'
