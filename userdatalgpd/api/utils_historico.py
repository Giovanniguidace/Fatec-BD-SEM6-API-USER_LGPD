
"""
Utils Histórico: Arquivo que contém todos os métodos de inserção de dados
em tabelas de histórico.
"""

from .models import *

def addHistoricoCriacaoUsuario(id_usuario, nome_completo, email):
    tb_historico_criacao_usuario = historico_criacao_usuario()
    tb_historico_criacao_usuario.id_usuario = id_usuario
    tb_historico_criacao_usuario.email = email
    tb_historico_criacao_usuario.nome_completo = nome_completo
    tb_historico_criacao_usuario.save()

def addHistoricoExclusaoUsuario(id_usuario, nome_completo, email):
    tb_historico_exclusao_usuario = historico_exclusao_usuario()
    tb_historico_exclusao_usuario.id_usuario = id_usuario
    tb_historico_exclusao_usuario.email = email
    tb_historico_exclusao_usuario.nome_completo = nome_completo
    tb_historico_exclusao_usuario.save()

def addHistoricoAtualizacaoUsuario(id_usuario, nome_completo, email):
    tb_historico_atualizacao_usuario = historico_atualizacao_usuario()
    tb_historico_atualizacao_usuario.id_usuario = id_usuario
    tb_historico_atualizacao_usuario.email = email
    tb_historico_atualizacao_usuario.nome_completo = nome_completo
    tb_historico_atualizacao_usuario.save()

def addHistoricoUsuarioTerceiro(id_usuario, cnpj_terceiro):
    tb_historico_usuario_terceiro = historico_usuario_terceiro()
    tb_historico_usuario_terceiro.id_usuario = id_usuario
    tb_historico_usuario_terceiro.cnpj_terceiro = cnpj_terceiro
    tb_historico_usuario_terceiro.save()

def addHistoricoAdicaoUsuarioTerceiroGrupo(id_usuario, cnpj_terceiro, nome_grupo):
    tb_historico_adicao_usuario_terceiro_grupo = historico_adicao_usuario_terceiro_grupo()
    tb_historico_adicao_usuario_terceiro_grupo.id_usuario = id_usuario
    tb_historico_adicao_usuario_terceiro_grupo.cnpj_terceiro = cnpj_terceiro
    tb_historico_adicao_usuario_terceiro_grupo.nome_grupo = nome_grupo
    tb_historico_adicao_usuario_terceiro_grupo.save()

def addHistoricoRemocaoUsuarioTerceiroGrupo(id_usuario, cnpj_terceiro, nome_grupo):
    tb_historico_remocao_usuario_terceiro_grupo = historico_remocao_usuario_terceiro_grupo()
    tb_historico_remocao_usuario_terceiro_grupo.id_usuario = id_usuario
    tb_historico_remocao_usuario_terceiro_grupo.cnpj_terceiro = cnpj_terceiro
    tb_historico_remocao_usuario_terceiro_grupo.nome_grupo = nome_grupo
    tb_historico_remocao_usuario_terceiro_grupo.save()


def addHistoricoAceiteUsuarioTermo(id_usuario, versao_termo, nome_termo, nome_completo_usuario):
    tb_historico_aceite_usuario_termo = historico_aceite_usuario_termo()
    tb_historico_aceite_usuario_termo.id_usuario = id_usuario
    tb_historico_aceite_usuario_termo.versao_termo = versao_termo
    tb_historico_aceite_usuario_termo.nome_termo = nome_termo
    tb_historico_aceite_usuario_termo.nome_completo_usuario = nome_completo_usuario
    tb_historico_aceite_usuario_termo.save()

