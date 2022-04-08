from rest_framework import generics
from django.shortcuts import render

from .models import *
# Create your views here.

from .serializers import *


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
