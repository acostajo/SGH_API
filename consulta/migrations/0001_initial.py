# Generated by Django 2.1.7 on 2019-02-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('codconsulta', models.AutoField(primary_key=True, serialize=False)),
                ('codficha', models.IntegerField()),
                ('codusuario', models.IntegerField()),
                ('fechaconsulta', models.DateField(auto_now=True)),
                ('diagnostico', models.CharField(max_length=80)),
                ('evolucion', models.CharField(max_length=80)),
                ('limitacion', models.CharField(max_length=80)),
                ('presionarte', models.IntegerField()),
                ('frescresp', models.IntegerField()),
                ('freccardia', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('talla', models.IntegerField()),
                ('nad', models.IntegerField()),
                ('nat', models.IntegerField()),
                ('eva', models.IntegerField()),
                ('vgp', models.IntegerField()),
                ('vgm', models.IntegerField()),
                ('cdai', models.IntegerField()),
                ('sdai', models.IntegerField()),
                ('haq', models.IntegerField()),
                ('das28pcr', models.IntegerField()),
                ('das28vsg', models.IntegerField()),
                ('sientepaci', models.IntegerField()),
                ('plan', models.CharField(max_length=80)),
                ('fechacreada', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('codconsulta',),
            },
        ),
    ]
