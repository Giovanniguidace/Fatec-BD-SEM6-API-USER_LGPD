from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usr_cpf = models.CharField("CPF", max_length=45, null=False)
    usr_telefone = models.CharField("Telefone", max_length=45, null=True)
    usr_conteudoMarketing = models.BooleanField("Aceita Marketing Opt-in Opt-out?", default=False)
    usr_aceitaCookies = models.BooleanField("Aceita Cookies?", default=False)
    usr_datacriacao = models.DateTimeField(auto_now_add=True, null=True)
    usr_dataatualizacao = models.DateTimeField(auto_now=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class tbTermo(models.Model):
    ter_id = models.AutoField("Termo ID", primary_key=True, )
    ter_nome = models.CharField("Nome Termo", max_length=45, null=False)
    
class tbVersaoTermo(models.Model):
    vte_id = models.AutoField("Versão Termo ID", primary_key=True)
    fk_ter_id = models.ForeignKey(tbTermo, verbose_name="ID Termo", on_delete=models.CASCADE, null=False)
    vte_versao = models.CharField("Versão Termo", max_length=10, null=False)
    vte_conteudo = models.CharField("Conteudo Termo", max_length=1000, null=False)

class tb_vte_usr(models.Model):
    vte_usr_id = models.AutoField("VTE X USR", primary_key=True)
    fk_usr_id = models.ForeignKey(User, null=False, verbose_name="ID Usuário", on_delete=models.CASCADE)
    fk_vte_id = models.ForeignKey(tbVersaoTermo, verbose_name="ID Versão Termo", on_delete=models.CASCADE)

    class Meta:
        unique_together = (('fk_usr_id', 'fk_vte_id'),)


class tbClienteExterno(models.Model):
    cle_cnpj = models.CharField('CNPJ', primary_key=True, max_length=20)
    cle_razaosocial = models.CharField('Razão Social', max_length=100, null=False)
    cle_unidade = models.CharField('Unidade', max_length=50, null=True)
    cle_ie = models.CharField('Inscrição Estadual', null=True, max_length=12)
    cle_im = models.CharField('Inscrição Municipal', null=True, max_length=11)
    cle_endereco = models.CharField('Endereço', max_length=150, null=False)
    cle_numero = models.CharField('Número', null=False, max_length=10)
    cle_complemento = models.CharField('Complemento', max_length=100, null=True)
    cle_bairro = models.CharField('Bairro', max_length=50, null=False)
    cle_cep = models.CharField('CEP', null=False, max_length=9)
    cle_cidade = models.CharField('Cidade', max_length=50, null=False)
    cle_uf = models.CharField('Estado', max_length=50, null=False)
    cle_fone1 = models.CharField('Telefone 1', null=False, max_length=13)
    cle_cel = models.CharField('Celular', null=True, max_length=14)
    cle_datacriacao = models.DateTimeField(auto_now_add=True, null=True)
    cle_dataatualizacao = models.DateTimeField(auto_now=True, null=True)


class tb_usr_cle(models.Model):
    usr_cle_id = models.AutoField("USR X CLE", primary_key=True)
    fk_usr_id = models.ForeignKey(User, verbose_name="Usuário ID", null=False, on_delete=models.CASCADE)
    fk_cle_cnpj = models.ForeignKey(tbClienteExterno, verbose_name="Cliente Externo ID", null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('fk_usr_id', 'fk_cle_cnpj'),)



class historico_criacao_usuario(models.Model):
    id = models.AutoField("id", primary_key=True)
    id_usuario = models.IntegerField("Id Usuário", null=False)
    nome_completo = models.CharField("Nome Usuário", max_length=100, null=False)
    email = models.CharField("Email Usuário", max_length=50, null=False)
    data_criacao = models.DateTimeField("Data Criação",auto_now_add=True, null=False)

class historico_exclusao_usuario(models.Model):
    id = models.AutoField("id", primary_key=True)
    id_usuario = models.IntegerField("Id Usuário", null=False)
    nome_completo = models.CharField("Nome Usuário", max_length=100, null=False)
    email = models.CharField("Email Usuário", max_length=50, null=False)
    data_exclusao = models.DateTimeField("Data Exclusão",auto_now_add=True, null=False)

class historico_atualizacao_usuario(models.Model):
    id = models.AutoField("id", primary_key=True)
    id_usuario = models.IntegerField("Id Usuário", null=False)
    nome_completo = models.CharField("Nome Usuário", max_length=100, null=False)
    email = models.CharField("Email Usuário", max_length=50, null=False)
    data_atualizacao = models.DateTimeField("Data Atualização",auto_now=True, null=False)

class historico_usuario_terceiro(models.Model):
    id = models.AutoField("id", primary_key=True)
    id_usuario = models.IntegerField("Id Usuário", null=False)
    cnpj_terceiro = models.CharField("Cnpj Terceiro", max_length=25, null=False)
    data_criacao = models.DateTimeField("Data Criação",auto_now_add=True, null=True)

class historico_adicao_usuario_terceiro_grupo(models.Model):
    id = models.AutoField("id", primary_key=True)
    id_usuario = models.IntegerField("Id Usuário", null=False)
    cnpj_terceiro = models.CharField("Cnpj Terceiro", max_length=25, null=False)
    nome_grupo = models.CharField("Nome Grupo", max_length=50, null=False)
    data_adicao = models.DateTimeField("Data Adição",auto_now_add=True, null=True)

class historico_remocao_usuario_terceiro_grupo(models.Model):
    id = models.AutoField("id", primary_key=True)
    id_usuario = models.IntegerField("Id Usuário", null=False)
    cnpj_terceiro = models.CharField("Cnpj Terceiro", max_length=25, null=False)
    nome_grupo = models.CharField("Nome Grupo", max_length=50, null=False)
    data_remocao = models.DateTimeField("Data Remoção", auto_now_add=True, null=True)

class historico_aceite_usuario_termo(models.Model):
    id = models.AutoField("id", primary_key=True)
    versao_termo = models.IntegerField("Versão Termo", null=False)
    nome_termo = models.CharField("Nome Termo", max_length=50, null=False)
    id_usuario = models.IntegerField("Id Usuário", null=False)
    nome_completo_usuario = models.CharField("Nome Usuário", max_length=100, null=False)
    data_aceite = models.DateTimeField("Data Aceite", auto_now_add=True, null=True)

