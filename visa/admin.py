from django.contrib import admin
from .models import Atividades, Perguntas

@admin.register(Atividades)
class AtividadesAdim(admin.ModelAdmin):
    list_display = ('cnae','atividade', 'grau_risco', 'num_pergunta', 'orgao')


@admin.register(Perguntas)
class PerguntasAdim(admin.ModelAdmin):
    list_display = ('numero','pergunta')