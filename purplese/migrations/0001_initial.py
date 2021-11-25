# Generated by Django 3.2.6 on 2021-11-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(help_text='Entre com a Categoria da sua imagem', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(help_text='Entre com a Genero da sua imagem', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(help_text='Entre com a Tag da sua imagem', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MeUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='static/img_upload')),
                ('descricao', models.TextField()),
                ('categoria', models.ManyToManyField(to='purplese.Categoria')),
                ('genero', models.ManyToManyField(to='purplese.Genero')),
                ('tag', models.ManyToManyField(to='purplese.Tag')),
            ],
        ),
    ]
