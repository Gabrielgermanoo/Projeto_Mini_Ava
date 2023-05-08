from lib2to3.pgen2.token import AT
from re import S
from django.contrib import admin
from .models import Atividade, Status, Classe, Question

# Register your models here.

admin.site.register(Atividade)
admin.site.register(Classe)
admin.site.register(Status)
admin.site.register(Question)