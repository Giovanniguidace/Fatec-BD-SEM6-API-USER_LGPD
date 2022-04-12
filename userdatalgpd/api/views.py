from urllib import request

from rest_framework import generics
from django.shortcuts import render

from .models import *
from django.contrib.auth.models import User
# Create your views here.

from .serializers import *

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response


from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def usersSystem_list(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            users = User.objects.all()
            serializer = userSystemSerializer(users, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = userSystemSerializer(data=request.data)
# PAREI AQUI
            if serializer.is_valid():
                for data in serializer:
                    user = User.objects.create_user(serializer)
                    print("data: ", data.name)
                    print("value: ", data.value)

                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'PUT', 'DELETE'])
def user_system(request, pk):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = userSystemSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = userSystemSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def profiles_list():
    profiles = Profile.objects.all()
    return profiles

class profilesApiView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = profileSerializer

class termosApiView(generics.ListCreateAPIView):
    queryset = tbTermo.objects.all()
    serializer_class = termoSerializer

class versoesTermosApiView(generics.ListCreateAPIView):
    queryset = tbVersaoTermo.objects.all()
    serializer_class = versaoTermoSerializer

class vteUsrApiView(generics.ListCreateAPIView):
    queryset = tb_vte_usr.objects.all()
    serializer_class = vteUsrSerializer

class clientesExternoApiView(generics.ListCreateAPIView):
    queryset = tbClienteExterno.objects.all()
    serializer_class = clienteExternoSerializer

class usrCleApiView(generics.ListCreateAPIView):
    queryset = tb_usr_cle.objects.all()
    serializer_class = usrCleSerializer

class cleGpaApiView(generics.ListCreateAPIView):
    queryset = tb_cle_gpa.objects.all()
    serializer_class = cleGpaSerializer
