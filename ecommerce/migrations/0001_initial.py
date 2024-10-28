# Generated by Django 5.1.2 on 2024-10-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CnpjEcommerce',
            fields=[
                ('id_cnpj', models.AutoField(primary_key=True, serialize=False)),
                ('number_cnpj', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'db_table': 'cnpj_numbers',
            },
        ),
    ]
