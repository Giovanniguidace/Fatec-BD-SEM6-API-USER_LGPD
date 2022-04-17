from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from .views import *

from rest_framework_simplejwt import views as jwt_views


urlpatterns = [

    # TERMOS
    path('termos/', getTermosView), # GET - POST

    path('termos/<str:pk>', getTermoView), # GET - PUT - DELETE
    path('versoesTermos/', getVersoesTermoView),  # GET - POST
    path('versoesTermos/<str:pk>', getVersaoTermoView), # GET - PUT - DELETE

    # TERMO X USUÁRIO
    path('termosUsuarios/', getVtesUsrsView),  # GET - POST
    path('termosUsuarios/<str:pk>', getVteUsrView), # GET - PUT - DELETE

    # USUÁRIOS
    path('usuarios/', getUsuariosView),  # GET - POST
    path('usuarios/<str:pk>', getUsuarioView), # GET - PUT - DELETE
    path('updateProfile/', getUsuarioView), # PUT


    # GRUPOS
    path('grupos/', getGroupsView),
    path('grupos/<str:pk>', getGroupView),

### TESTAR IMPLEMENTAÇÃO DAS ROTAS ABAIXO
    # CLIENTES EXTERNOS X USUÁRIOS
    path('clientesExternosUsuarios/', getUsrsClesView),
    path('clientesExternosUsuarios/<str:pk>', getUsrCleView),

    # CLIENTES EXTERNOS
    path('clientesExternos/', getClientesExternosView),
    path('clientesExternos/<str:pk>', getClienteExternoView),




    # GET TOKEN - MÉTODO POST - NECESSITA FORNECER CREDENCIAIS username=username password=password
    #path('api-token-auth/', views.obtain_auth_token),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),




]
