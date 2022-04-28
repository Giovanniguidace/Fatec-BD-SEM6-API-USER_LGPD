
"""
Utils Histórico: Arquivo que contém todos os métodos de inserção de dados
em tabelas de histórico.
"""

from .models import *

##### MÉTODOS PARA A INSERÇÃO DE DADOS NAS TABELAS DE HISTÓRICO

def historicoCriacaoUsuario(id_usuario, nome_completo, email):
    hist_criacao_usuario = historico_criacao_usuario()
    hist_criacao_usuario.id_usuario = id_usuario
    hist_criacao_usuario.nome_completo = nome_completo
    hist_criacao_usuario.email = email
    hist_criacao_usuario.save()

def historicoExclusaoUsuario(id_usuario, nome_completo, email):
    hist_exclusao_usuario = historico_exclusao_usuario()
    hist_exclusao_usuario.id_usuario = id_usuario
    hist_exclusao_usuario.nome_completo = nome_completo
    hist_exclusao_usuario.email = email
    hist_exclusao_usuario.save()

def historicoAtualizacaoUsuario(id_usuario, nome_completo, email):
    hist_atualizacao_usuario = historico_atualizacao_usuario()
    hist_atualizacao_usuario.id_usuario = id_usuario
    hist_atualizacao_usuario.nome_completo = nome_completo
    hist_atualizacao_usuario.email = email
    hist_atualizacao_usuario.save()

def historicoUsuarioTerceiro(id_usuario, cnpj_terceiro):
    hist_usuario_terceiro = historico_usuario_terceiro()
    hist_usuario_terceiro.id_usuario = id_usuario
    hist_usuario_terceiro.cnpj_terceiro = cnpj_terceiro
    hist_usuario_terceiro.save()

def historicoAdicaoUsuarioTerceiroGrupo(id_usuario, cnpj_terceiro, nome_grupo):
    hist_adicao_usuario_terceiro_grupo = historico_adicao_usuario_terceiro_grupo()
    hist_adicao_usuario_terceiro_grupo.id_usuario = id_usuario
    hist_adicao_usuario_terceiro_grupo.cnpj_terceiro = cnpj_terceiro
    hist_adicao_usuario_terceiro_grupo.nome_grupo = nome_grupo
    hist_adicao_usuario_terceiro_grupo.save()

def historicoRemocaoUsuarioTerceiroGrupo(id_usuario, cnpj_terceiro, nome_grupo):
    hist_remocao_usuario_terceiro_grupo = historico_remocao_usuario_terceiro_grupo()
    hist_remocao_usuario_terceiro_grupo.id_usuario = id_usuario
    hist_remocao_usuario_terceiro_grupo.cnpj_terceiro = cnpj_terceiro
    hist_remocao_usuario_terceiro_grupo.nome_grupo = nome_grupo
    hist_remocao_usuario_terceiro_grupo.save()

def historicoAceiteUsuarioTermo(versao_termo, nome_termo, id_usuario, nome_completo_usuario):
    hist_aceite_usuario_termo = historico_aceite_usuario_termo()
    hist_aceite_usuario_termo.versao_termo = versao_termo
    hist_aceite_usuario_termo.nome_termo = nome_termo
    hist_aceite_usuario_termo.id_usuario = id_usuario
    hist_aceite_usuario_termo.nome_completo_usuario = nome_completo_usuario
    hist_aceite_usuario_termo.save()

