from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_distplay = ("id","qusetion_title")


admin.site.register(Question, QuestionAdmin)