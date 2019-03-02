# Generated by Django 2.1.7 on 2019-03-02 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManiExtraArti',
            fields=[
                ('codmanif', models.AutoField(primary_key=True, serialize=False)),
                ('codusuario', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('fechacreada', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('codmanif',),
            },
        ),
    ]
