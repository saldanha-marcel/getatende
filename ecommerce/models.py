from django.db import models

class CnpjEcommerce(models.Model):
    id_cnpj = models.AutoField(primary_key=True, verbose_name='Id')  
    number_cnpj = models.CharField(max_length=25, unique=True, verbose_name='CNPJ')

    def __str__(self):
        return self.number_cnpj

    class Meta:
        db_table = 'cnpj_numbers'
        verbose_name = 'CNPJ'
