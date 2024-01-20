from django.db import models
from django.urls import reverse
from django.conf import settings


# modelo da tabela para planilhas de exercícios (contém nome da planilha, criador e uma lista de exercícios)
class ExerciseSheet(models.Model):
    name = models.CharField(max_length=60)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)
    exercises = models.ManyToManyField('Exercise')

    # método para retornar string que será mostrada na página de admin
    def __str__(self):
        return self.name

    # método para retornar a URL de uma instância dessa tabela (útil para templates)
    """exemplo: um template que lista todas as planilhas com hyperlinks, que se clicados levam a uma url com o
    id dessa planilha, que pode ser configurada como uma rota para um template específico dessa planilha"""

    def get_absolute_url(self):
        return reverse('sheet_detail', args=str(self.id))


# modelo da tabela para os exercícios (contém nome do exercício, descrição e quem adicionou o exercício)
class Exercise(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=200)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercise_detail', args=[str(self.id)])
