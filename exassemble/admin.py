from django.contrib import admin
from .models import Exercise, ExerciseSheet


# registra o modelo para exercícios na página de admin
admin.site.register(Exercise)


# registra o modelo para planilhas de exercícios na página admin e cria customização para a exibição dela
@admin.register(ExerciseSheet)
class AdminSheet(admin.ModelAdmin):
    # estiliza a forma e quais campos da tabela de planilhas aparecerão na página admin
    fieldsets = [
        (None, {"fields" : ["name", "creator"],},),
        ("Lista de Exercícios", {"classes" : ["collapse", "wide"], "fields" : ["exercises"],},),
    ]
