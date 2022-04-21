# Generated by Django 4.0.3 on 2022-04-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_profile_usr_aceitacookies_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='historico_aceite_usuario_termo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('versao_termo', models.IntegerField(verbose_name='Versão Termo')),
                ('nome_termo', models.CharField(max_length=50, verbose_name='Nome Termo')),
                ('id_usuario', models.IntegerField(verbose_name='Id Usuário')),
                ('nome_completo_usuario', models.CharField(max_length=100, verbose_name='Nome Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='historico_adicao_usuario_terceiro_grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('id_usuario', models.IntegerField(verbose_name='Id Usuário')),
                ('cnpj_terceiro', models.CharField(max_length=25, verbose_name='Cnpj Terceiro')),
                ('nome_grupo', models.CharField(max_length=50, verbose_name='Nome Grupo')),
                ('data_adicao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data Adição')),
            ],
        ),
        migrations.CreateModel(
            name='historico_atualizacao_usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('id_usuario', models.IntegerField(verbose_name='Id Usuário')),
                ('nome_completo', models.CharField(max_length=100, verbose_name='Nome Usuário')),
                ('email', models.CharField(max_length=50, verbose_name='Email Usuário')),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data Atualização')),
            ],
        ),
        migrations.CreateModel(
            name='historico_criacao_usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('id_usuario', models.IntegerField(verbose_name='Id Usuário')),
                ('nome_completo', models.CharField(max_length=100, verbose_name='Nome Usuário')),
                ('email', models.CharField(max_length=50, verbose_name='Email Usuário')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
            ],
        ),
        migrations.CreateModel(
            name='historico_exclusao_usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('id_usuario', models.IntegerField(verbose_name='Id Usuário')),
                ('nome_completo', models.CharField(max_length=100, verbose_name='Nome Usuário')),
                ('email', models.CharField(max_length=50, verbose_name='Email Usuário')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
            ],
        ),
        migrations.CreateModel(
            name='historico_remocao_usuario_terceiro_grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('id_usuario', models.IntegerField(verbose_name='Id Usuário')),
                ('cnpj_terceiro', models.CharField(max_length=25, verbose_name='Cnpj Terceiro')),
                ('nome_grupo', models.CharField(max_length=50, verbose_name='Nome Grupo')),
                ('data_remocao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data Remoção')),
            ],
        ),
        migrations.CreateModel(
            name='historico_terceiro_sem_usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('cnpj_terceiro', models.CharField(max_length=25, verbose_name='Cnpj Terceiro')),
            ],
        ),
        migrations.CreateModel(
            name='historico_usuario_terceiro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('id_usuario', models.IntegerField(verbose_name='Id Usuário')),
                ('cnpj_terceiro', models.CharField(max_length=25, verbose_name='Cnpj Terceiro')),
                ('data_adicao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data Adição')),
            ],
        ),
    ]