from django.db import models

class SerialNumber(models.Model):
    id_serial = models.AutoField(primary_key=True, verbose_name='Id')  
    number_serial = models.CharField(max_length=255, unique=True, verbose_name='Serial')

    def __str__(self):
        return self.number_serial

    class Meta:
        db_table = 'serial_numbers'
        verbose_name = 'Número de Série'