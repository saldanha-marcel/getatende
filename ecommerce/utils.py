import csv
from .models import CnpjEcommerce

def importar_dados_csv(arquivo_csv):
    leitor = csv.DictReader(arquivo_csv.read().decode('utf-8').splitlines())
    for linha in leitor:
        CnpjEcommerce.objects.create(
            number_cnpj=linha['number_cnpj']
        )