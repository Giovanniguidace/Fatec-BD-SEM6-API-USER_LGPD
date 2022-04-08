from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usr_cpf = models.CharField("CPF", max_length=45, null=False)
    usr_telefone = models.CharField("Telefone", max_length=45, null=True)
    usr_datacriacao = models.DateTimeField(auto_now_add=True, null=True)
    usr_dataatualizacao = models.DateTimeField(auto_now=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class tbTermo(models.Model):
    ter_id = models.IntegerField("Termo ID", primary_key=True)
    ter_nome = models.CharField("Nome Termo", max_length=45, null=False)
    
class tbVersaoTermo(models.Model):
    vte_id = models.IntegerField("Versão Termo ID", primary_key=True)
    fk_ter_id = models.ForeignKey(tbTermo, verbose_name="ID Termo", on_delete=models.CASCADE, null=False)
    vte_versao = models.CharField("Versão Termo", max_length=10, null=False)
    vte_conteudo = models.CharField("Conteudo Termo", max_length=1000, null=False)

class tb_vte_usr(models.Model):
    vte_usr_id = models.IntegerField("VTE X USR", primary_key=True)
    fk_usr_id = models.ForeignKey(User, null=False, verbose_name="ID Usuário", on_delete=models.CASCADE)
    fk_vte_id = models.ForeignKey(tbVersaoTermo, verbose_name="ID Versão Termo", on_delete=models.CASCADE)

    class Meta:
        unique_together = (('fk_usr_id', 'fk_vte_id'),)


class tbClienteExterno(models.Model):
    cle_cnpj = models.CharField('CNPJ', primary_key=True, max_length=14)
    cle_razaosocial = models.CharField('Razão Social', max_length=100, null=False)
    cle_unidade = models.CharField('Unidade', max_length=50, null=True)
    cle_ie = models.CharField('Inscrição Estadual', null=True, max_length=12)
    cle_im = models.CharField('Inscrição Municipal', null=True, max_length=11)
    cle_endereco = models.CharField('Endereço', max_length=150, null=False)
    cle_numero = models.IntegerField('Número', null=False)
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
    usr_cle_id = models.IntegerField("USR X CLE", primary_key=True)
    fk_usr_id = models.ForeignKey(User, verbose_name="Usuário ID", null=False, on_delete=models.CASCADE)
    fk_cle_cnpj = models.ForeignKey(tbClienteExterno, verbose_name="Cliente Externo ID", null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('fk_usr_id', 'fk_cle_cnpj'),)

class tb_cle_gpa(models.Model):
    cle_gpa_id = models.IntegerField("CLE X GPA", primary_key=True)
    fk_cle_cnpj = models.ForeignKey(tbClienteExterno, verbose_name="Cnpj Cliente Externo", on_delete=models.CASCADE, null=False)
    fk_gpa_id = models.ForeignKey(Group, verbose_name="Grupo Acesso ID", on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = (('fk_cle_cnpj', 'fk_gpa_id'),)

