# Generated by Django 4.0.3 on 2022-04-28 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_historico_aceite_usuario_termo_data_aceite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_adicao_usuario_terceiro_grupo',
            name='cnpj_terceiro',
            field=models.CharField(max_length=50, verbose_name='Cnpj Terceiro'),
        ),
        migrations.AlterField(
            model_name='historico_remocao_usuario_terceiro_grupo',
            name='cnpj_terceiro',
            field=models.CharField(max_length=50, verbose_name='Cnpj Terceiro'),
        ),
    ]
