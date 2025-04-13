from django.contrib import admin
from .models import Question, Choice

# Inline para Choice
class ChoiceInline(admin.TabularInline):  # también podés usar StackedInline
    model = Choice
    extra = 3  # cantidad de opciones vacías por defecto

# Configuración del admin de Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Registro
admin.site.register(Question, QuestionAdmin)