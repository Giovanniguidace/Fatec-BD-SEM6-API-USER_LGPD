"""
Métodos que serão utilizados pelas views.
"""
import json
from .insert_db import *
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token

from .utils_historico import *

message_401 = "Acesso Restrito: Você não possui direitos de acesso a este recurso!"

# VALIDA SE PK EXISTE
def checkPK(pk, table):
    valida_pk = table.objects.filter(pk=pk).exists()
    if valida_pk == True:
        getOne = table.objects.get(pk=pk)
        return getOne
    elif valida_pk == False:
        return valida_pk


def getAllTable(table, ModelSerializer):
    dados_tabela = table.objects.all()
    serializer = ModelSerializer(dados_tabela, many=True)
    return Response(serializer.data)

def postData(request, ModelSerializer):
    serializer = ModelSerializer(data=request.data)

    if "usrCleSerializer" in str(ModelSerializer):
        id_usuario = request.data.get('fk_usr_id')
        cnpj_terceiro = request.data.get('fk_cle_cnpj')
        historicoUsuarioTerceiro(id_usuario, cnpj_terceiro)

    if "vteUsrSerializer" in str(ModelSerializer):
        get_vte = tbVersaoTermo.objects.get(vte_id=request.data.get('fk_vte_id'))
        versao_termo = get_vte.vte_versao
        nome_termo = get_vte.fk_ter_id.ter_nome
        id_usuario = request.data.get('fk_usr_id')
        user = User.objects.get(id=id_usuario)
        nome_completo_usuario = user.first_name + " " + user.last_name
        historicoAceiteUsuarioTermo(versao_termo, nome_termo, id_usuario, nome_completo_usuario)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# MÉTODO DE INICIAZALIÇÃO NAS VIEWS
def getAllList(request, table, ModelSerializer, grupo_view):
    valida_grupo = False
    for grupo in request.user.groups.all():
        if grupo == grupo_view:
            valida_grupo = True

    if request.method == 'GET':
        if request.user.is_superuser or valida_grupo == True:
            return getAllTable(table, ModelSerializer)
        else:
            return Response(message_401, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'POST' or valida_grupo == True:
        if request.user.is_superuser or request.user.groups.get(name=grupo_view).exists():
            return postData(request, ModelSerializer)
        else:
            return Response(message_401, status=status.HTTP_401_UNAUTHORIZED)


def getOneTable(get_data, ModelSerializer):
    serializer = ModelSerializer(get_data)
    return Response(serializer.data)

def updateOneTable(request,get_data, ModelSerializer):
    serializer = ModelSerializer(get_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

def deleteOneTable(get_data):
    get_data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# GET DOS DADOS DE DETERMINADO ID DE DETERMINADO MODEL
def getOneList(request, pk, table, ModelSerializer, grupo_view):
    valida_grupo = False
    for grupo in request.user.groups.all():
        if grupo == grupo_view:
            valida_grupo = True

    get_data = checkPK(pk, table)

    if get_data == False:
        return Response("ID inexistente!! ", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if request.user.is_superuser or valida_grupo == True:
            return getOneTable(get_data, ModelSerializer)
        else:
            return Response(message_401, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'PUT':
        if request.user.is_superuser or valida_grupo == True:
            return updateOneTable(request,get_data, ModelSerializer)
        else:
            return Response(message_401, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'DELETE':
        if request.user.is_superuser or valida_grupo == True:
            return deleteOneTable(get_data)
        else:
            return Response(message_401, status=status.HTTP_401_UNAUTHORIZED)


def createUser(request, User):
    password = request.data.get('password')
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    username = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name,email=email)
    id_user = User.objects.get(username=username).id
    profile = Profile.objects.get(user=id_user)
    data_profile = request.data.get('profile')
    for index, (key, value) in enumerate(data_profile.items()):
        if key == "usr_cpf":
            profile.usr_cpf = value
        if key == "usr_telefone":
             profile.usr_telefone = value
    profile.save()

    return username


def updateUser(request, pk,getOne, User, ModelSerializer):
    getOne.set_password(request.data.get('password'))
    getOne.username = request.data.get('username')
    getOne.first_name = request.data.get('first_name')
    getOne.last_name = request.data.get('last_name')
    getOne.email = request.data.get('email')
    getOne.save()

    profile = Profile.objects.get(user=pk)
    data_profile = request.data.get('profile')
    for index, (key, value) in enumerate(data_profile.items()):
        if key == "usr_cpf":
            profile.usr_cpf = value
        if key == "usr_telefone":
            profile.usr_telefone = value
    profile.save()

    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ModelSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

def getAllUsers(request, table, readOnlyUserSerializer , UserSerializer):
    if request.user.is_superuser:
        if request.method == 'GET':
            table = table.objects.all()
            serializer = readOnlyUserSerializer(table, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                username = createUser(request, table)
                user = table.objects.get(username=username)
                nome_completo = user.first_name + " " + user.last_name
                historicoCriacaoUsuario(user.id, nome_completo, user.email)

                serializer = readOnlyUserSerializer(user)
                print(user.id, nome_completo, user.email)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(message_401, status=status.HTTP_401_UNAUTHORIZED)

def getOneUser(request, pk, table, readOnlyUserSerializer, UserSerializer):
    if request.user.is_superuser:

        getOne = checkPK(pk, table)

        if getOne == False:
            return Response("ID inexistente!! ", status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(id=pk)
        nome_completo = user.first_name + " " + user.last_name

        if request.method == 'GET':
            serializer = readOnlyUserSerializer(getOne)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UserSerializer(getOne, data=request.data)
            if serializer.is_valid():
                historicoAtualizacaoUsuario(pk, nome_completo, user.email)
                return updateUser(request, pk, getOne, table, readOnlyUserSerializer)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            historicoExclusaoUsuario(pk, nome_completo, user.email)
            getOne.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(message_401, status=status.HTTP_401_UNAUTHORIZED)

def addRemoveUsrGrupo(request, usrGpaSerializer, groupsUserSerializer, acao):
    if request.user.is_superuser:
        if request.method == 'POST':
            # VALIDAR SE USUÁRIO E GRUPO EXISTE
            id_user = request.data.get('id_user')
            group_name = request.data.get('group_name')
            try:
                user = User.objects.get(id=id_user)
                grupo = Group.objects.get(name=group_name)
            except:
                return Response("Usuário ou Grupo inexistente!",status=status.HTTP_404_NOT_FOUND)

            # VALIDAR SE USUÁRIO É TERCEIRO
            validaUsuarioTerceiro = tb_usr_cle.objects.filter(fk_usr_id=user.id).exists()

            # CASO EXISTA, REALIZAR A ADIÇÃO OU EXCLUSÃO
            serializer = usrGpaSerializer(data=request.data)
            if serializer.is_valid():
                if acao == "ADICIONAR":

                    grupo.user_set.add(user)
                    serializer = groupsUserSerializer(user)

                    #INSERIR HISTÓRICO DE CRIAÇÃO
                    if validaUsuarioTerceiro == True:
                        cnpj_terceiro = tb_usr_cle.objects.get(fk_usr_id=user.id).fk_cle_cnpj.cle_cnpj
                        print("cnpj_terceiro: ", cnpj_terceiro)
                        historicoAdicaoUsuarioTerceiroGrupo(user.id, cnpj_terceiro, grupo.name)


                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                elif acao == "EXCLUIR":
                    grupo.user_set.remove(user)
                    serializer = groupsUserSerializer(user)

                    # INSERIR HISTÓRICO DE REMOÇÃO
                    if validaUsuarioTerceiro == True:
                        cnpj_terceiro = tb_usr_cle.objects.get(fk_usr_id=user.id).fk_cle_cnpj.cle_cnpj
                        historicoRemocaoUsuarioTerceiroGrupo(user.id, cnpj_terceiro, grupo.name)

                    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
          return Response(message_401, status=status.HTTP_401_UNAUTHORIZED)



def addUsuarioGrupo(request,usrGpaSerializer, groupsUserSerializer):
    acao = "ADICIONAR"
    return addRemoveUsrGrupo(request, usrGpaSerializer, groupsUserSerializer, acao)


def removeUsuarioGrupo(request,usrGpaSerializer, groupsUserSerializer):
    acao = "EXCLUIR"
    return addRemoveUsrGrupo(request, usrGpaSerializer, groupsUserSerializer, acao)


