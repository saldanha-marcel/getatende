from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import SerialNumber
from .serializers import SerialSerializer

import json

from . import utils as fn

@api_view(['GET', 'POST'])
def get_or_create_serial(request, number_serial=None):
    # Para requisições GET, buscar o número serial
    print(request.data)
    if request.method == 'GET' and number_serial is not None:
        try:
            serial = SerialNumber.objects.get(number_serial=number_serial)
            serializer = SerialSerializer(serial) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SerialNumber.DoesNotExist:
            return Response({
                'error': 'Number serial not found'
            }, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        seriais = SerialNumber.objects.all()
        serializer = SerialSerializer(seriais, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SerialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def create_multiple_serials(request):
    print(request.data)
    """ Função para incluir vários números de série. """
    if 'numbers' not in request.data:
        print(request)
        return Response({'error': 'Field "numbers" is required.'}, status=status.HTTP_400_BAD_REQUEST)

    numbers = request.data['numbers']
    # Separando os números pelo caractere vírgula e removendo espaços extras
    numbers_list = [number.strip() for number in numbers.split(',')]

    created_serials = []  # Lista para armazenar os números de série criados
    errors = []  # Lista para armazenar erros

    for number in numbers_list:
        serializer = SerialSerializer(data={'number_serial': number})
        if serializer.is_valid():
            serializer.save()  # Salva o número serial no banco
            created_serials.append(serializer.data)
        else:
            errors.append(serializer.errors)

    if errors:
        return Response({'created_serials': created_serials, 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'created_serials': created_serials}, status=status.HTTP_201_CREATED)