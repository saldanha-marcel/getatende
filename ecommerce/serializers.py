from rest_framework import serializers

from .models import CnpjEcommerce

class CnpjSerializer(serializers.ModelSerializer):
    class Meta:
        model = CnpjEcommerce
        fields = ['id_cnpj', 'number_cnpj']