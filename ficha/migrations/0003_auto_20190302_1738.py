# Generated by Django 2.1.7 on 2019-03-02 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0002_auto_20190224_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('codpaciente', models.AutoField(primary_key=True, serialize=False)),
                ('codusuario', models.IntegerField()),
                ('nombres', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('cedula', models.CharField(max_length=10, null=True, unique=True)),
                ('sexo', models.CharField(max_length=1)),
                ('fechainclusion', models.DateField()),
                ('procedencia', models.CharField(max_length=80)),
                ('nacionalidad', models.CharField(max_length=80)),
                ('escolaridad', models.CharField(max_length=80)),
                ('diagnostico', models.CharField(max_length=80)),
                ('fechadiagnos', models.DateField()),
                ('fechanaci', models.DateField()),
                ('estadocivil', models.CharField(max_length=20)),
                ('profesion', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('lineabaja', models.CharField(max_length=20)),
                ('fechacreada', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('codpaciente',),
            },
        ),
        migrations.AlterField(
            model_name='ficha',
            name='codpaciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ficha.Paciente'),
        ),
    ]
