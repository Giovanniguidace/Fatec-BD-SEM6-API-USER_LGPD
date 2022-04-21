from urllib import request

from rest_framework import generics
from django.shortcuts import render

from .models import *
from .utils import *
from django.contrib.auth.models import User, Group
# Create your views here.

from .serializers import *

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response


from rest_framework.decorators import api_view


""" 
VIEWS: Views referente ao gerenciamento de usuários do sistema.
"""

@api_view(['GET', 'POST'])
def getUsuariosView(request):
   return getAllUsers(request, User, readOnlyUserSerializer, UserSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getUsuarioView(request, pk):
    return getOneUser(request,pk,User, readOnlyUserSerializer, UserSerializer)


"""
VIEWS: Views referente ao cadastro de termos e versões dos termos no qual cada usuário realizará a aceitação
via sistema.
"""

@api_view(['GET', 'POST'])
def getTermosView(request):
    grupo_view = "READ_TERMOS"
    return getAllList(request, tbTermo, termoSerializer, grupo_view)

@api_view(['GET', 'PUT', 'DELETE'])
def getTermoView(request, pk):
    grupo_view = "READ_TERMOS"
    return getOneList(request, pk, tbTermo, termoSerializer, grupo_view)

@api_view(['GET', 'POST'])
def getVersoesTermoView(request):
    grupo_view = "READ_TERMOS"
    return getAllList(request, tbVersaoTermo, versaoTermoSerializer, grupo_view)

@api_view(['GET', 'PUT', 'DELETE'])
def getVersaoTermoView(request, pk):
    grupo_view = "READ_TERMOS"
    return getOneList(request, pk, tbVersaoTermo, versaoTermoSerializer, grupo_view)


"""
VIEWS: View referente à relação entre Versão do Termo e Usuários
"""

@api_view(['GET', 'POST'])
def getVtesUsrsView(request):
    grupo_view = ""
    return getAllList(request, tb_vte_usr, vteUsrSerializer, grupo_view)

@api_view(['GET', 'PUT', 'DELETE'])
def getVteUsrView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, tb_vte_usr, vteUsrSerializer, grupo_view)


"""
VIEWS: Views referente ao cadastro de clientes externos que terão acesso à API.
"""

@api_view(['GET', 'POST'])
def getClientesExternosView(request):
    grupo_view = "READ_CLIENTES_EXTERNOS"
    return getAllList(request, tbClienteExterno, clienteExternoSerializer, grupo_view)

@api_view(['GET', 'PUT', 'DELETE'])
def getClienteExternoView(request, pk):
    grupo_view = "READ_CLIENTES_EXTERNOS"
    return getOneList(request, pk, tbClienteExterno, clienteExternoSerializer, grupo_view)


"""
VIEWS: Views referente à relação de Usuários e Clientes Externo. Cada cliente externo possui um
usuário de acesso com token.
"""

@api_view(['GET', 'POST'])
def getUsrsClesView(request):
    grupo_view = ""
    return getAllList(request, tb_usr_cle, usrCleSerializer, grupo_view)

@api_view(['GET', 'PUT', 'DELETE'])
def getUsrCleView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, tb_usr_cle, usrCleSerializer, grupo_view)



"""
VIEWS: Views referente à criação de grupos de acesso de Usuários. Permitida a criação 
apenas por administradores do sistema.
"""

@api_view(['GET', 'POST'])
def getGroupsView(request):
    grupo_view = ""
    return getAllList(request, Group, groupSystemSerializer, grupo_view)

@api_view(['GET', 'PUT', 'DELETE'])
def getGroupView(request,pk):
    grupo_view = ""
    return getOneList(request,pk, Group, groupSystemSerializer, grupo_view)

@api_view(['POST'])
def addUserGroupView(request):
    return addUsuarioGrupo(request,usrGpaSerializer, groupsUserSerializer)

@api_view(['POST'])
def removeUserGroupView(request):
    return removeUsuarioGrupo(request,usrGpaSerializer, groupsUserSerializer)

