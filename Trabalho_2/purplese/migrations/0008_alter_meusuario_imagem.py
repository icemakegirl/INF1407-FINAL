# Generated by Django 3.2.6 on 2021-11-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purplese', '0007_alter_meusuario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meusuario',
            name='imagem',
            field=models.ImageField(default=2, max_length=500, upload_to='static/img_upload/'),
            preserve_default=False,
        ),
    ]
