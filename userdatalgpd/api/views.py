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

"""
VIEWS: Views referente à consulta de históricos.
"""

## HISTÓRICO DA CRIAÇÃO DE USUÁRIO
@api_view(['GET'])
def getAllHistoricoCriacaoUsuarioView(request):
    grupo_view = ""
    return getAllList(request, historico_criacao_usuario, historicoCriacaoUsuarioSerializer, grupo_view)

@api_view(['GET'])
def getOneHistoricoCriacaoUsuarioView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, historico_criacao_usuario, historicoCriacaoUsuarioSerializer, grupo_view)

## HISTÓRICO DA EXCLUSÃO DE USUÁRIO
@api_view(['GET'])
def getAllHistoricoExclusaoUsuarioView(request):
    grupo_view = ""
    return getAllList(request, historico_exclusao_usuario, historicoExclusaoUsuarioSerializer, grupo_view)

@api_view(['GET'])
def getOneHistoricoExclusaoUsuarioView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, historico_exclusao_usuario, historicoExclusaoUsuarioSerializer, grupo_view)

## HISTÓRICO DA ATUALIZAÇÃO DE USUÁRIO
@api_view(['GET'])
def getAllAtualizacaoExclusaoUsuarioView(request):
    grupo_view = ""
    return getAllList(request, historico_atualizacao_usuario, historicoAtualizacaoUsuarioSerializer, grupo_view)

@api_view(['GET'])
def getOneHistoricoAtualizacaoUsuarioView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, historico_atualizacao_usuario, historicoAtualizacaoUsuarioSerializer, grupo_view)

## HISTÓRICO DE USUÁRIO TERCEIRO
@api_view(['GET'])
def getAllHistoricoUsuariosTerceiroView(request):
    grupo_view = ""
    return getAllList(request, historico_usuario_terceiro, historicoUsuarioTerceiroSerializer, grupo_view)

@api_view(['GET'])
def getOneHistoricoUsuarioTerceiroView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, historico_usuario_terceiro, historicoUsuarioTerceiroSerializer, grupo_view)

## HISTÓRICO DE ADIÇÃO DE USUÁRIO TERCEIRO EM GRUPO DE USUÁRIO
@api_view(['GET'])
def getAllHistoricoAdicaoUsuarioTerceiroGrupoView(request):
    grupo_view = ""
    return getAllList(request, historico_adicao_usuario_terceiro_grupo, historicoAdicaoUsuarioTerceiroGrupoSerializer, grupo_view)

@api_view(['GET'])
def getOneHistoricoAdicaoUsuarioTerceiroGrupoView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, historico_adicao_usuario_terceiro_grupo, historicoAdicaoUsuarioTerceiroGrupoSerializer, grupo_view)

## HISTÓRICO DE REMOÇÃO DE USUÁRIO TERCEIRO EM GRUPO DE USUÁRIO
@api_view(['GET'])
def getAllHistoricoRemocaoUsuarioTerceiroGrupoView(request):
    grupo_view = ""
    return getAllList(request, historico_remocao_usuario_terceiro_grupo, historicoRemocaoUsuarioTerceiroGrupoSerializer, grupo_view)

@api_view(['GET'])
def getOneHistoricoRemocaoUsuarioTerceiroGrupoView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, historico_remocao_usuario_terceiro_grupo, historicoRemocaoUsuarioTerceiroGrupoSerializer, grupo_view)

## HISTÓRICO DE ACEITE DE TERMO PELO USUÁRIO
@api_view(['GET'])
def getAllHistoricoAceiteUsuarioTermoView(request):
    grupo_view = ""
    return getAllList(request, historico_aceite_usuario_termo, historicoAceiteUsuarioTermoSerializer, grupo_view)

@api_view(['GET'])
def getOneHistoricoAceiteUsuarioTermoView(request, pk):
    grupo_view = ""
    return getOneList(request, pk, historico_aceite_usuario_termo, historicoAceiteUsuarioTermoSerializer, grupo_view)





