# Generated by Django 3.0.3 on 2020-03-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_orcamento', '0004_cadastroorcamento_obs_cadastro_orcamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastroorcamento',
            name='aprovacao',
            field=models.BooleanField(default=False),
        ),
    ]
