# Generated by Django 3.0.3 on 2020-03-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas_a_pagar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaapagar',
            name='anexo_boleto_contas_a_pagar',
            field=models.FileField(blank=True, null=True, upload_to='anexo_boleto/'),
        ),
        migrations.AlterField(
            model_name='contaapagar',
            name='anexo_comprovante_contas_a_pagar',
            field=models.FileField(blank=True, null=True, upload_to='anexo_comprovante/'),
        ),
    ]
