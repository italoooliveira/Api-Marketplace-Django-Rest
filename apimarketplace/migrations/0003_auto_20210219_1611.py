# Generated by Django 3.1.6 on 2021-02-19 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apimarketplace', '0002_auto_20210219_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtoimagem',
            name='url',
        ),
        migrations.AddField(
            model_name='produtoimagem',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 2, 19, 16, 11, 57, 259103)),
        ),
    ]
