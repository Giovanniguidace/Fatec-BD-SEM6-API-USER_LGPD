from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *



urlpatterns = [
    path('termos/', termosApiView.as_view(), name='termos'),
    path('versoesTermos/', versoesTermosApiView.as_view(), name='versoes_termos'),
    path('versaoTermosUsuarios/', vteUsrApiView.as_view(), name='versao_termos_usuarios'),
    path('clientesExternos/', clientesExternoApiView.as_view(), name='clientes_externos'),
    path('usuarioClientesExternos/', usrCleApiView.as_view(), name='usuario_clientes_externos'),
    path('clientesExternosGrupoAcesso/', cleGpaApiView.as_view(), name='clientes_externos_grupo_acesso'),

]
