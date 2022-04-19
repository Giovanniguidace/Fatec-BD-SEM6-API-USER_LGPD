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

@api_view(['PUT'])
def putProfile(request, pk):
    return getAllList(request,pk, profileSerializer, readOnlyUserSerializer)


"""
VIEWS: Views referente ao cadastro de termos e versões dos termos no qual cada usuário realizará a aceitação
via sistema.
"""

@api_view(['GET', 'POST'])
def getTermosView(request):
    return getAllList(request, tbTermo, termoSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getTermoView(request, pk):
    return getOneList(request, pk, tbTermo, termoSerializer)

@api_view(['GET', 'POST'])
def getVersoesTermoView(request):
    return getAllList(request, tbVersaoTermo, versaoTermoSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getVersaoTermoView(request, pk):
    return getOneList(request, pk, tbVersaoTermo, versaoTermoSerializer)


"""
VIEWS: View referente à relação entre Versão do Termo e Usuários
"""

@api_view(['GET', 'POST'])
def getVtesUsrsView(request):
    return getAllList(request, tb_vte_usr, vteUsrSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getVteUsrView(request, pk):
    return getOneList(request, pk, tb_vte_usr, vteUsrSerializer)


"""
VIEWS: Views referente ao cadastro de clientes externos que terão acesso à API.
"""

@api_view(['GET', 'POST'])
def getClientesExternosView(request):
    return getAllList(request, tbClienteExterno, clienteExternoSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getClienteExternoView(request, pk):
    return getOneList(request, pk, tbClienteExterno, clienteExternoSerializer)


"""
VIEWS: Views referente à relação de Usuários e Clientes Externo. Cada cliente externo possui um
usuário de acesso com token.
"""

@api_view(['GET', 'POST'])
def getUsrsClesView(request):
    return getAllList(request, tb_usr_cle, usrCleSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getUsrCleView(request, pk):
    return getOneList(request, pk, tb_usr_cle, usrCleSerializer)



"""
VIEWS: Views referente à criação de grupos de acesso de Usuários. Permitida a criação 
apenas por administradores do sistema.
"""

@api_view(['GET', 'POST'])
def getGroupsView(request):
    return getAllList(request, Group, groupSystemSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getGroupView(request):
    return getOneList(request, Group, groupSystemSerializer)
