from lib2to3.pgen2.token import AT
from re import S
from django.contrib import admin
from .models import Campo, Atividade, Campus, Status, Classe

# Register your models here.

admin.site.register(Campo)
admin.site.register(Atividade)
admin.site.register(Classe)
admin.site.register(Campus)
admin.site.register(Status)