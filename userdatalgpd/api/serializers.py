from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User, Group
from django.db import models

class groupSystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id',
            'name'
        )

class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'user',
            'usr_cpf',
            'usr_telefone',
            'usr_datacriacao',
            'usr_dataatualizacao'
        )

class readOnlyUserSerializer(serializers.ModelSerializer):
    profile = profileSerializer(Profile.objects.all())
    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined',
            'groups',
            'profile'
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined'
        )


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
            'cle_cnpj',
            'cle_razaosocial',
            'cle_unidade',
            'cle_ie',
            'cle_im',
            'cle_endereco',
            'cle_numero',
            'cle_complemento',
            'cle_bairro',
            'cle_cep',
            'cle_cidade',
            'cle_uf',
            'cle_fone1',
            'cle_cel',
            'cle_datacriacao',
            'cle_dataatualizacao'
        )

class usrCleSerializer(serializers.ModelSerializer):

    class Meta:
        model = tb_usr_cle
        fields = (
            'usr_cle_id',
            'fk_usr_id',
            'fk_cle_cnpj'
        )

class usrGpaSerializer(serializers.Serializer):
    id_user = serializers.IntegerField()
    group_name = serializers.CharField()

    class Meta:
        fields = (
            'id_user',
            'group_name'
        )

class groupsUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'groups'
        )