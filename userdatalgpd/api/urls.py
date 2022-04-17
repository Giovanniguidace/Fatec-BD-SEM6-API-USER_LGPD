from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *



urlpatterns = [

    # TERMOS
    path('termos/', getTermosView),
    path('termos/<str:pk>', getTermoView),
    path('versoesTermos/', getVersoesTermoView),
    path('versoesTermos/<str:pk>', getVersaoTermoView),

    # TERMO X USUÁRIO
    path('termosUsuarios/', getVtesUsrsView),
    path('termosUsuarios/<str:pk>', getVteUsrView),

    # USUÁRIOS
    path('usuarios/', getUsuariosView),
    path('usuarios/<str:pk>', getUsuarioView),
    path('profiles/', getProfiles),

### TESTAR IMPLEMENTAÇÃO DAS ROTAS ABAIXO
    # CLIENTES EXTERNOS X USUÁRIOS
    path('clientesExternosUsuarios/', getUsrsClesView),
    path('clientesExternosUsuarios/<str:pk>', getUsrCleView),

    # CLIENTES EXTERNOS
    path('clientesExternos/', getClientesExternosView),
    path('clientesExternos/<str:pk>', getClienteExternoView),

    # CLIENTES EXTERNOS X GRUPOS

]
