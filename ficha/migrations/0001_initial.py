# Generated by Django 2.1.7 on 2019-02-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('codficha', models.AutoField(primary_key=True, serialize=False)),
                ('codpaciente', models.IntegerField()),
                ('codpatron', models.IntegerField()),
                ('codusuario', models.IntegerField()),
                ('nhc', models.IntegerField()),
                ('iniciosint', models.DateField()),
                ('formainic', models.CharField(max_length=50)),
                ('apf', models.CharField(max_length=50)),
                ('apfcv', models.CharField(max_length=50)),
                ('appfractura', models.CharField(max_length=50)),
                ('apffractura', models.CharField(max_length=50)),
                ('protesissitio', models.CharField(max_length=50)),
                ('protefecha', models.DateField()),
                ('apfneoplasias', models.IntegerField()),
                ('sedentarismo', models.BooleanField()),
                ('actifisica', models.BooleanField()),
                ('tabaqfecha', models.DateField()),
                ('tabnumero', models.IntegerField()),
                ('extabaq', models.BooleanField()),
                ('menarca', models.IntegerField()),
                ('menopausia', models.IntegerField()),
                ('edadvidasex', models.IntegerField()),
                ('gestas', models.IntegerField()),
                ('partos', models.IntegerField()),
                ('cesareas', models.IntegerField()),
                ('abortos', models.IntegerField()),
                ('hisjospost', models.BooleanField()),
                ('factorreuma', models.IntegerField()),
                ('acp', models.IntegerField()),
                ('acp_nivel', models.IntegerField()),
                ('rxmanos', models.BooleanField()),
                ('rxmanosfecha', models.DateField()),
                ('rxpies', models.BooleanField()),
                ('rxpiesfecha', models.DateField()),
                ('fechacreadaa', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('fechacreadaa',),
            },
        ),
    ]
