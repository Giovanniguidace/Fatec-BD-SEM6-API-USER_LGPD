from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *



urlpatterns = [
    path('termos/', termosApiView.as_view(), name='termos'),
    #path('termos/(?P<pk>[0-9]+)$', termoApiView.as_view(), name='termo'),
    #path('profiles/', profilesApiView.as_view(), name='profiles'),
    path('usersSystem/', usersSystem_list, name='users'),
    path('usersSystem/<str:pk>', user_system, name='user'),
    path('profiles/', profiles_list, name='profiles'),
    #path('profiles/(?P<pk>[0-9]+)$', profileApiView.as_view(), name='profile'),
    path('versoesTermos/', versoesTermosApiView.as_view(), name='versoes_termos'),
    #path('versoesTermos/(?P<pk>[0-9]+)$', versaoTermosApiView.as_view(), name='versão_termo'),
    path('versaoTermosUsuarios/', vteUsrApiView.as_view(), name='versao_termos_usuarios'),
    #path('versaoTermosUsuarios/(?P<pk>[0-9]+)$', oneVteUsrApiView.as_view(), name='versao_termos_usuario'),
    path('clientesExternos/', clientesExternoApiView.as_view(), name='clientes_externos'),
    #path('clientesExternos/(?P<pk>[0-9]+)$', clienteExternoApiView.as_view(), name='cliente_externos'),
    path('usuarioClientesExternos/', usrCleApiView.as_view(), name='usuario_clientes_externos'),
    #path('usuarioClientesExternos/(?P<pk>[0-9]+)$', oneUsrCleApiView.as_view(), name='usuario_cliente_externo'),
    path('clientesExternosGrupoAcesso/', cleGpaApiView.as_view(), name='clientes_externos_grupo_acesso'),
    #path('clientesExternosGrupoAcesso/(?P<pk>[0-9]+)$', oneCleGpaApiView.as_view(), name='cliente_externo_grupo_acesso'),

]
