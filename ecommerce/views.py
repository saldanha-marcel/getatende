from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import CnpjEcommerce
from .serializers import CnpjSerializer

import json


@api_view(['GET', 'POST'])
def get_or_create_cnpj(request, number_cnpj=None):
    if request.method == 'GET' and number_cnpj is not None:
        try:
            serial = CnpjEcommerce.objects.get(number_cnpj=number_cnpj)
            serializer = CnpjSerializer(serial) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CnpjEcommerce.DoesNotExist:
            return Response({
                'error': 'Number serial not found'
            }, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        seriais = CnpjEcommerce.objects.all()
        serializer = CnpjSerializer(seriais, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CnpjSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def create_multiple_cnpjs(request):
    if 'numbers' not in request.data:
        return Response({'error': 'Field "numbers" is required.'}, status=status.HTTP_400_BAD_REQUEST)

    numbers = request.data['numbers']

    numbers_list = [number.strip() for number in numbers.split(',')]

    created_cnpjs = []
    errors = []

    for number in numbers_list:
        serializer = CnpjSerializer(data={'number_cnpj': number})
        if serializer.is_valid():
            serializer.save() 
            created_cnpjs.append(serializer.data)
        else:
            errors.append(serializer.errors)

    if errors:
        return Response({'created_cnpjs': created_cnpjs, 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'created_cnpjs': created_cnpjs}, status=status.HTTP_201_CREATED)