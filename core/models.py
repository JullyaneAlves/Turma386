from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
#/mysite/core/models.py

from django.db import models

class Agenda(models.Model):
    data = models.DateField('data do evento')
    hora = models.TimeField('horário')
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.titulo


class Autor(models.Model):
    class Meta:
        verbose_name_plural = 'autores'

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)

    def __str__(self):
        return self.sobrenome.upper() + ',' + self.nome


class Aluno(models.Model):
    matricula = models.CharField(max_length=12, unique=True)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return "{}, ({})".format(self.titulo, self.ano_publicacao)


class Emprestimo(models.Model):
    usuario = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    livros = models.ManyToManyField(Livro)
    devolvido = models.BooleanField()

    def __str__(self):
        return self.usuario
    
    
    class Contato(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Livraria(models.Model):
    Titulo = models.CharField(max_length=105)
    Nome_do_autor = models.CharField(max_length=70)
    Assunto = models.CharField(max_length=50)
    Editora = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    Publicacao = models.DateField()


    def __str__(self):
        return self.Titulo

class Despesa(models.Model):
    data_criacao = models.CharField(max_length=35)
    tipo_despesa = models.CharField(max_length=50)
    descricao = models.CharField(max_length=60)
    forma_pagamento = models.CharField(max_length=40)
    vencimento = models.DateField()
    quitado = models.BooleanField()


    def __str__(self):
        return self.data_criacao

class Compras(models.Model):
    nome = models.CharField(max_length=80)
    descricaoProduto = models.CharField(max_length=95)
    qtdPrevistoMes = models.FloatField()
    preco = models.FloatField()
    precoMaximo = models.FloatField()

    def __str__(self):
        return self.nome

class Apartamento(models.Model):
    numero = models.IntegerField()
    qtdQuartoss = models.IntegerField()
    proprietario = models.CharField(max_length=80)
    valorCondominio = models.FloatField()

    def __str__(self):
        return self.numero

class Anuncio(models.Model):
    cliente = models.CharField(max_length=90)
    textoTitulo = models.CharField(max_length=80)
    preco = models.IntegerField()
    textoAnuncio = models.CharField(max_length=150)
    nomeContato = models.CharField(max_length=60)
    telefone = models.CharField(max_length=20)
    secao = models.CharField(max_length=25)
    tipoAnuncio = models.CharField(max_length=35)

    def __str__(self):
        return self.cliente

