from django.contrib import admin

from .models import *

# Register your models here.

#### TABELA CLIENTE #######
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'usr_cpf',
        'usr_telefone',
        'usr_datacriacao',
        'usr_dataatualizacao'
    ]

admin.site.register(Profile, ProfileAdmin)

#################################