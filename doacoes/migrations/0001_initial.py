# Generated by Django 5.0 on 2023-12-08 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id_doacao', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.TextField()),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='media/')),
                ('status', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doacoes.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
