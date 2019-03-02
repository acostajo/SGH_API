# Generated by Django 2.1.7 on 2019-03-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comorbilidad',
            fields=[
                ('codcomor', models.AutoField(primary_key=True, serialize=False)),
                ('codenfermedad', models.IntegerField()),
                ('codficha', models.IntegerField()),
                ('fechadiagnostico', models.DateField()),
            ],
            options={
                'ordering': ('codcomor',),
            },
        ),
    ]