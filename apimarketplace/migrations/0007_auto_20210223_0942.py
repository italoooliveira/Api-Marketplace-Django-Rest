# Generated by Django 3.1.6 on 2021-02-23 12:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apimarketplace', '0006_auto_20210222_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id_loja', models.AutoField(primary_key=True, serialize=False)),
                ('nome_loja', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14)),
                ('cep', models.CharField(max_length=25)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('endereco', models.CharField(blank=True, max_length=100, null=True)),
                ('numero', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 2, 23, 9, 41, 59, 617890)),
        ),
        migrations.AddField(
            model_name='categoria',
            name='id_loja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apimarketplace.loja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_loja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apimarketplace.loja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='id_loja',
            field=models.ManyToManyField(to='apimarketplace.Loja'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_loja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apimarketplace.loja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='id_loja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apimarketplace.loja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxaentrega',
            name='id_loja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apimarketplace.loja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transportadora',
            name='id_loja',
            field=models.ManyToManyField(to='apimarketplace.Loja'),
        ),
    ]