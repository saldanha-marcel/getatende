from rest_framework import serializers

from .models import SerialNumber

class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialNumber
        fields = ['id_serial', 'number_serial']