from django.contrib import admin

from .models import Agenda
from .models import Livraria
from .models import  Despesa
from .models import Compras
from .models import Apartamento
from .models import Anuncio

from .models import *

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'data_nascimento')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_retirada', 'aluno', 'devolvido')
    filter_horizontal = ['livros']

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)



class AgendaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')


admin.site.register(Agenda, AgendaAdmin)

class LivrariaAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'Nome_do_autor', 'Assunto', 'Editora', 'ISBN')

admin.site.register(Livraria, LivrariaAdmin)


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

admin.site.register(Contato, ContatoAdmin)


class  DespesaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao' , 'tipo_despesa', 'descricao', 'forma_pagamento' )

admin.site.register(Despesa,  DespesaAdmin)


class ComprasAdmin(admin.ModelAdmin):
    list_display = ('nome' , 'descricaoProduto')

admin.site.register(Compras, ComprasAdmin)


class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'proprietario')

admin.site.register(Apartamento, ApartamentoAdmin)

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('cliente' , 'textoTitulo', 'textoAnuncio', 'nomeContato', 'telefone', 'secao', 'tipoAnuncio')

admin.site.register(Anuncio, AnuncioAdmin)






