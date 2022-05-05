from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Perguntas(models.Model):
    numero = models.CharField(max_length=3)
    pergunta = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ('numero',)
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return self.numero


class Atividades(models.Model):
    cnae = models.CharField(max_length=10)
    atividade = models.CharField(max_length=500)
    grau_risco = models.CharField(max_length=100)
    num_pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE)
    orgao = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.atividade