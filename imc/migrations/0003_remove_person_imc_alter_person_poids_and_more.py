# Generated by Django 4.1.3 on 2022-11-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imc', '0002_alter_person_imc_alter_person_poids_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='imc',
        ),
        migrations.AlterField(
            model_name='person',
            name='poids',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='taille',
            field=models.CharField(max_length=50),
        ),
    ]