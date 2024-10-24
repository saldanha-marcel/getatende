from django.db import models

class SerialNumber(models.Model):
    id_serial = models.AutoField(primary_key=True)  
    number_serial = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.number_serial

    class Meta:
        db_table = 'serial_numbers'
