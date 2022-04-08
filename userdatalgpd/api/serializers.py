from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User

""" 
class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            
        )
"""

class termoSerializer(serializers.ModelSerializer):

    class Meta:
        model = tbTermo
        fields = (
            'ter_id',
            'ter_nome'
        )

class versaoTermoSerializer(serializers.ModelSerializer):

    class Meta:
        model = tbVersaoTermo
        fields = (
            'vte_id',
            'fk_ter_id',
            'vte_versao',
            'vte_conteudo'
        )

class vteUsrSerializer(serializers.ModelSerializer):

    class Meta:
        model = tb_vte_usr
        fields = (
            'vte_usr_id',
            'fk_usr_id',
            'fk_vte_id'
        )

class clienteExternoSerializer(serializers.ModelSerializer):

    class Meta:
        model = tbClienteExterno
        fields = (
            '__all__',
        )

class usrCleSerializer(serializers.ModelSerializer):

    class Meta:
        model = tb_usr_cle
        fields = (
            'usr_cle_id',
            'fk_usr_id',
            'fk_cle_cnpj'
        )

class cleGpaSerializer(serializers.ModelSerializer):

    class Meta:
        model = tb_cle_gpa
        fields = (
            'cle_gpa_id',
            'fk_cle_cnpj',
            'fk_gpa_id'
        )