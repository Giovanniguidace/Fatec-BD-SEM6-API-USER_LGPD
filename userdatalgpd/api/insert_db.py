
from .serializers import groupSystemSerializer
from django.contrib.auth.models import Group

# CREATE GROUPS
grupos = [ "READ_USERS",
           "READ_PROFILES",
           "READ_LOGS",
           "READ_CLIENTES_EXTERNOS",
           "READ_TERMOS",
           "READ_HISTORICOS",
           ]

def createGroups():
    for grupo in grupos:
        Group.objects.get_or_create(name=grupo)

createGroups()

