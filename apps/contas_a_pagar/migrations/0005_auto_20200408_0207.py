# Generated by Django 3.0.3 on 2020-04-08 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas_a_pagar', '0004_auto_20200408_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaapagar',
            name='status_contas_a_pagar',
            field=models.CharField(choices=[('C', 'Criado'), ('A1', 'Aprovação 1'), ('A2', 'Aprovação 2'), ('AP', 'Aprovado'), ('EF', 'Evolução Fiscal'), ('EFF', 'Eviar Financeiro'), ('BX', 'Baixado')], default='C', max_length=3),
        ),
    ]
