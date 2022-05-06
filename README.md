# Projeto - SEM6 - Tópicos Avançados em Banco de Dados - Prof. Sakaue - Fatec SJC Prof. Jessen Vidal.


# API - Gerenciamento de Usuários respeitando a LGPD



## :orange_book: <b>Desafio apresentado:</b>

Implementar alternativas de solução decorrentes da implantação da LGPD.


## <b>:dart: Objetivo da Aplicação</b>

O objetivo da aplicação é atender a LGPD nos quesitos abaixo:

* Sistema de Gerenciamento de Usuários;
* Termos de Responsabilidade;
* Opt-In e Opt-Out;
* Históricos;
* Cadastro de Terceiro que terão acesso à API;
* Autenticação utilizando Bearer Token;
* Controle de acesso à rotas através de grupos de usuário;



## <b>⚙️ Tecnologias Adotadas na Solução:</b>

* [Python 3.8.10](https://www.python.org/)
* [Django 4.0.3](https://www.djangoproject.com/)
* [Django Rest Framework 3.13.1](https://www.django-rest-framework.org/)
* [PostgreSQL 14.2](https://www.postgresql.org/)
* [MySQL WorkBench](https://www.mysql.com/products/workbench/)
* [PostMan (Para Testes)](https://www.postman.com/)
* [PsycoPG2 2.9.3](https://pypi.org/project/psycopg2/)
* [PyJWT 2.3.0](https://pyjwt.readthedocs.io/en/stable/)


## <b> :wrench: Desenvolvimento da Aplicação: </b>

### Mapa mental da aplicação:

![https://user-images.githubusercontent.com/62898187/166472375-1b8a37ad-86d6-4faa-8322-078513c25b6c.png](https://user-images.githubusercontent.com/62898187/166472375-1b8a37ad-86d6-4faa-8322-078513c25b6c.png)
### Modelo Entidade Relacionamento - MER

![MER - User Data](https://user-images.githubusercontent.com/62898187/166472834-8882d427-6914-4a38-a5db-1e5164e15db9.png)

### Autenticação utilizando Bearer Token:

Para que a API seja acessada de forma segura, foi realizada a criação de autenticação através de Bearer Token, onde o Token gerado se expira a cada 5 minutos, havendo a necessidade de um Refresh e assim continuar o acesso à API.

Esta forma de segurança é a mais utilizada no mercado. Só pelo fato da utilização do Token, já nos traz segurança, mas pelo fato de atualizar a cada 5 minutos para cada sessão, nos traz uma segurança ainda maior.

Este método é comumente indicado por equipes de segurança da informação para atender exigências da LGPD.

Exemplo de Token para utilização na API:
![image](https://user-images.githubusercontent.com/62898187/167137456-58c1bdd8-45a9-4a09-b13e-301871471f1d.png)
Este é um exemplo de como obter o Bearer Token de acesso à API, onde é necessário passar as credenciais de usuário utilizando o método POST.

A aplicação fornecerá dois tipos de token, o "access" e o "refresh". O token access é o token para utilização nas requisições, com validade de 5 minutos. O token refresh é para renovar o token access. 

Neste exemplo, estamos utilizando usuário super admin da aplicação, mas também poderá ser obtido por usuários que são vinculados a clientes terceiros.

Como forma de assegurar ainda mais o controle de acesso, mesmo que o cliente terceiro tenha o token, ele só conseguirá acessar determinada rota caso seja adicionado em determinado grupo.

Para que o token seja utilizado nas rotas da API, ele deverá ser adicionado como "Authorization: Bearer token".

Segue abaixo exemplo de acesso não autorizado ou token expirado:
![image](https://user-images.githubusercontent.com/62898187/167150240-08e11a8d-2545-4ca1-8d8b-06046aeba24c.png)

Para a criação deste sistema de Token, foi utilizada a biblioteca PyJWT 2.3.0 integrada ao Django.

### Sistema de Gerenciamento de Usuários:

Para este objetivo, foi desenvolvido um sistema de criação, atualização, deleção de usuários da aplicação, onde temos 3 tipos de usuários, são eles: Usuários comuns; Usuários Adm's; Usuários Terceiros;

Cada usuário possui suas credenciais de acesso, com senha criptografada.

A cada movimentação deste usuário, é registrado a data e horário de criação, atualização e exclusão, garantindo assim, as exigências da LGPD.

Exemplo de usuário criado:

![image](https://user-images.githubusercontent.com/62898187/167139008-3ecdf2e2-f94c-4402-a78d-ed54acd059e5.png)
Neste exemplo, conseguimos verificar que a senha é criptografada, trazendo uma segurança ainda maior para os acessos à aplicação.
Também, é possível verificar os dados do "Profile" deste usuário e também em quais grupos ele está inserido. Este usuário, é um usuário comum, portanto não poderá ser incluido em nenhum grupo. 

É possível verificar também que existe a data de criação do usuário, data de criação do profile e a atualização do usuário. Desta forma, conseguiremos obter dados com exatidão para atender alguns requisitos da LGPD.

Exemplo de usuário sendo atribuido à um terceiro:

![image](https://user-images.githubusercontent.com/62898187/167139940-83a2217c-fcd3-430b-9dc3-12fe069da3a7.png)
Neste exemplo, é possível verificar que podemos atribuir um usuário ou mais para um cliente terceiro. Desta forma, conseguiremos obter uma rastreabilidade eficiente de qual usuário está vinculado a determinado cliente.

### Termos de Responsabilidade:

Foi desenvolvido um sistema de controle de termos de responsabilidade do usuário, onde é possível criar o termo e versões do termo, para caso haja a necessidade de atualização do mesmo.

Os usuários possuem a opção de assinar o termo ou não.

Exemplo de termos criados:
![image](https://user-images.githubusercontent.com/62898187/167140723-4059fe2d-a7e7-4859-9b78-047b5e1badc5.png)
Neste exemplo, é mostrado todos os termos criados na aplicação, onde este será vinculado à versões de termo, onde assim conseguiremos ter quantas versões quisermos de um deteminado termo. Isso será de extrema ajuda para garantir a normalização do banco de dados.

Exemplo de versões de termo:
![image](https://user-images.githubusercontent.com/62898187/167141244-5231bc49-b7fa-4251-a00a-0e70f7a3a775.png)
Neste exemplo, é mostrado todas as versões vinculadas à termos criados. É possível ter mais de uma versão para um determinado termo, e também é possível vincular usuários nestas determinadas versões, confirmando sua assinatura a determinado termo e versão. 

Exemplo de usuário vinculado a versão de termo:
![image](https://user-images.githubusercontent.com/62898187/167142333-e5af4ffb-b878-4279-b466-38115749c693.png)
Neste exemplo, é mostrado todos os usuários vinculados a versões de termos, garantindo que determinado usuário assinou o termo em determinada versão.


### Opt-In e Opt-Out:

Cada usuário possui a opção de aceitar o Opt-In Opt-Out, e com isso, foi disponibilizada no perfil do usuário uma opção Booleana para que seja ativada essa opção ou não.

O aceite ou não aceite fica registrado no próprio profile do usuário, onde é true para aceito e false para não aceito. Segue abaixo um exemplo:
![image](https://user-images.githubusercontent.com/62898187/167148580-85e09042-898e-4522-a60c-513cc6b06bbf.png)
Observe que temos o campo "usr_conteudoMarketing", onde é nele que determina se o usuário aceita Opt-in Opt-out. 

Também foi adicionado a opção de aceitar ou não a coleta de Cookies de sessão.

### Cadastro de Terceiro que terão acesso à API:

Foi desenvolvido um sistema de controle de acesso à API feita por Terceiros, onde é possível, com segurança, fornecer nossa API para clientes.

Tudo se inicia no cadastramento do terceiro, com dados de CNPJ; Razão Social e etc... Após esta etapa, é realizada a criação de um usuário do sistema, onde este será vinculado ao terceiro. 

Exemplo de cadastro de terceiro:
![image](https://user-images.githubusercontent.com/62898187/167149441-1b3362f8-dc1b-45fc-95b0-a477d8566770.png)
Neste exemplo, é possível observar que é feito um cadastro completo do cliente terceiro, coletando todas as suas informações. É possível verificar a data de criação e atualização.

Conforme já mencionado em exemplos acima, é possível vincular esse cliente terceiro a um ou mais usuários da aplicação, onde estes serão incluidos em grupos que determinarão quais rotas poderão acessar.

O usuário terceiro não possui acesso à rota de usuários ou profiles, onde este só é acessado por super users.


### Controle de acesso à rotas através de grupos de usuário:

Foi realizado um sistema de controle de acesso à API por grupos, onde as rotas são classificadas e disponibilizadas de acordo com a necessidade de cada cliente.

Esta forma de configuração traz segurança, onde o usuário terceiro só terá acesso à aquele recurso se ele realmente tiver a necessidade de acessar.

O cadastramento de usuários terceiro em grupos só é realizada por usuários administradores.

Exemplos de grupos:

* READ_USERS;
* READ_PROFILES;
* READ_LOGS;
* READ_CLIENTES_EXTERNOS;
* READ_TERMOS;
* READ_HISTORICOS;

Exemplo de cadastro de grupos:
![image](https://user-images.githubusercontent.com/62898187/167150541-b9d07f08-6df7-4818-b8a5-5c834380bf56.png)
Neste exemplo, é possível observar os grupos que foram cadastrados na aplicação, onde estes serão vinculados a usuários para acesso à API em rotas específicas de cada grupo.

Exemplo de usuário vinculado a grupos:
![image](https://user-images.githubusercontent.com/62898187/167150956-99d2265a-f6f2-473d-ba8d-ccec5d3c19a3.png)
Como podemos observar, o usuário de id 12 está inserido no grupo de id 7, que se chama "READ_TERMOS", permitindo que este usuário consiga acessar as rotas referentes a termos e versões de termos.

Exemplo de usuário que tentou acessar determinada rota sem estar inserido em grupo:

1º Gerar token de acesso do usuário id 12 que possue acesso apenas para termos:
![image](https://user-images.githubusercontent.com/62898187/167151926-a83d9f0b-9384-4adf-947c-bc4b2819a0d1.png)
2º Tentativa de acessar rota para coleta de clientes terceiros:
![image](https://user-images.githubusercontent.com/62898187/167151985-a563b8e9-3350-4fcd-9204-fa7ec5e2fc1f.png)

Com isso, garantimos a segurança no acesso às informações, uma das regras principais da LGPD.

### Históricos:

Para atender as exigências da LGPD, foi desenvolvido um sistema de históricos, onde temos configurados os seguintes históricos:

* Criação de Usuário;
![image](https://user-images.githubusercontent.com/62898187/167152984-be3da89d-3029-4b92-b9f0-91bfeb7d1fce.png)

* Exclusão de Usuário;
![image](https://user-images.githubusercontent.com/62898187/167153138-d080afc2-a5e7-4a12-ab45-126d7c8938e3.png)
* Atualização de Usuário;
![image](https://user-images.githubusercontent.com/62898187/167153325-3a064429-4641-46e8-8b93-4ecf9071ab14.png)

* Usuários Terceiro;
![image](https://user-images.githubusercontent.com/62898187/167153793-5be46d2d-4bcc-403d-9d09-be6c122e687d.png)

* Adição de usuário terceiro em grupo de acesso;

![image](https://user-images.githubusercontent.com/62898187/167154061-f5e4cc15-6b40-4f29-9ff3-39d438bd2969.png)
* Remoção de usuário terceiro em grupo de acesso;
![image](https://user-images.githubusercontent.com/62898187/167154266-5b55b9da-892c-4612-aaed-9f4a6c28a9bf.png)

* Aceite de usuário em relação ao termo de responsabilidade;
![image](https://user-images.githubusercontent.com/62898187/167154440-377b5e2b-6abd-489f-8efb-6a9b1f00bbe0.png)

## :zap: Execução da Aplicação


### Iniciando o projeto 

Neste projeto, foi configurado banco de dados PostgreSQL localmente. Para que seja possível executar esta aplicação em outra máquina, será preciso criar o banco de acordo com a seguinte configuração:

```python
DATABASES = {  
  'default': {  
  'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'db_userlgpd',  
        'USER': 'postgres',  
        'PASSWORD': 'pg@123',  
        'HOST': 'localhost',  
        'PORT': '5432',  
    }  
}
```

As credenciais de acesso poderão ser configuradas da forma como desejar.

Após a criação do banco e inserção das configurações de acesso no arquivo settings.py, é preciso migrar os models do projeto para o banco de dados, com o seguinte comando:

```python
python manage.py migrate
```

Após executar este comando, é preciso criar um Super User, com o seguinte comando:

```python
python3 manage.py createsuperuser
```

Este usuário possuirá acesso total à aplicação.


Para executar a aplicação, digite o seguinte comando:

```cmd
python3 manage.py runserver
```



OBS.: É preciso executar estes comandos na raiz do projeto, onde o arquivo manage.py está localizado.




