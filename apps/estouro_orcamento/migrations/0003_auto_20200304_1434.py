# Generated by Django 3.0.3 on 2020-03-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estouro_orcamento', '0002_cadastroestouroorcamento_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroestouroorcamento',
            name='status',
            field=models.CharField(choices=[('C', 'Criado'), ('A1', 'Aprovação 1'), ('A2', 'Aprovação 2'), ('AP', 'Aprovado')], default='C', max_length=2),
        ),
    ]
