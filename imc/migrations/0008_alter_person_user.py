# Generated by Django 4.1.3 on 2023-06-10 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imc', '0007_person_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
