# Generated by Django 5.1.2 on 2024-10-24 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SerialNumber',
            fields=[
                ('id_serial', models.AutoField(primary_key=True, serialize=False)),
                ('number_serial', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'serial_numbers',
            },
        ),
    ]
