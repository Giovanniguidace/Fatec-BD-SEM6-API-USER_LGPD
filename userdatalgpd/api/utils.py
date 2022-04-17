"""
Métodos que serão utilizados pelas views.
"""
import json

from rest_framework import status
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from .models import Profile
# VALIDA SE PK EXISTE
def checkPK(pk, table):
    try:
        getOne = table.objects.get(pk=pk)
        return getOne
    except getOne.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# GET DE TODOS OS VALORES DE DETERMINADO MODEL
def getAllList(request, table, ModelSerializer):
    if request.user.is_authenticated:
        if request.method == 'GET':
            versoesTermos = table.objects.all()
            serializer = ModelSerializer(versoesTermos, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ModelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# GET DOS DADOS DE DETERMINADO ID DE DETERMINADO MODEL
def getOneList(request, pk, table, ModelSerializer):
    if request.user.is_authenticated:
        getOne = checkPK(pk, table)
        if request.method == 'GET':
            serializer = ModelSerializer(getOne)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ModelSerializer(getOne, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            getOne.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)




def createUser(request, User, ModelSerializer):
    password = request.data.get('password')
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    username = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name,email=email)
    return username


def updateUser(request, pk,getOne, User, ModelSerializer):
    getOne.set_password(request.data.get('password'))
    getOne.username = request.data.get('username')
    getOne.first_name = request.data.get('first_name')
    getOne.last_name = request.data.get('last_name')
    getOne.email = request.data.get('email')
    getOne.save()
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ModelSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

def getAllUsers(request, table, readOnlyUserSerializer , UserSerializer):
    if request.user.is_authenticated:
        if request.method == 'GET':
            table = table.objects.all()
            serializer = readOnlyUserSerializer(table, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                username = createUser(request, table, UserSerializer)
                try:
                    user = table.objects.get(username=username)
                except table.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = readOnlyUserSerializer(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


def getOneUser(request, pk, table, readOnlyUserSerializer, UserSerializer):
    if request.user.is_authenticated:
        getOne = checkPK(pk, table)
        if request.method == 'GET':
            serializer = readOnlyUserSerializer(getOne)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UserSerializer(getOne, data=request.data)
            if serializer.is_valid():
                return updateUser(request, pk, getOne, table, UserSerializer)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            getOne.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

# PAREI AQUI
def updateProfile(request, User, profileSerializer, readOnlyUserSerializer):
         if request.method == 'PUT':
            serializer = profileSerializer(data=request.data)
            if serializer.is_valid():
                id_user =  request.data.get('user')
                usr_cpf =  request.data.get('usr_cpf')
                usr_telefone =  request.data.get('usr_telefone')
                profile = Profile()
                profile.user = User.objects.get(id=id_user)
                profile.usr_cpf = usr_cpf
                profile.usr_telefone = usr_telefone
                profile.save()
                serializer = readOnlyUserSerializer(User.objects.get(id=id_user))
                return Response(serializer.data ,status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
