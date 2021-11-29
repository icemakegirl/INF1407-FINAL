# Generated by Django 3.2.6 on 2021-11-25 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purplese', '0003_auto_20211124_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meusuario',
            name='categoria',
        ),
        migrations.AddField(
            model_name='meusuario',
            name='categoria',
            field=models.CharField(default=2, help_text='Entre com a Categoria da sua imagem', max_length=40),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='meusuario',
            name='genero',
        ),
        migrations.AddField(
            model_name='meusuario',
            name='genero',
            field=models.CharField(default=1, help_text='Entre com a Genero da sua imagem', max_length=40),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='meusuario',
            name='tag',
        ),
        migrations.AddField(
            model_name='meusuario',
            name='tag',
            field=models.CharField(default=2, help_text='Entre com a Tag da sua imagem', max_length=40),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
