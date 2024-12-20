# Generated by Django 4.2.17 on 2024-12-06 14:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editora', models.CharField(max_length=50)),
                ('local', models.CharField(default='Brasil', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(default='Desconhecido', max_length=50)),
                ('ano', models.IntegerField(default=2024)),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.editora')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserva_id', models.IntegerField()),
                ('data_reserva', models.DateField(default=django.utils.timezone.now)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emprestimo_id', models.IntegerField()),
                ('data_emprestimo', models.DateField(default=django.utils.timezone.now)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('editora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.editora')),
            ],
        ),
    ]
