# Generated by Django 3.2.6 on 2021-11-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purplese', '0006_alter_meusuario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meusuario',
            name='imagem',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='static/img_upload/'),
        ),
    ]