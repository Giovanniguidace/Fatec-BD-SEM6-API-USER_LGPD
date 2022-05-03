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

### Sistema de Gerenciamento de Usuários:

Para este objetivo, foi desenvolvido um sistema de criação, atualização, deleção de usuários da aplicação, onde temos 3 tipos de usuários, são eles: Usuários comuns; Usuários Adm's; Usuários Terceiros;

Cada usuário possui suas credenciais de acesso, com senha criptografada.

A cada movimentação deste usuário, é registrado a data e horário de criação, atualização e exclusão, garantindo assim, as exigências da LGPD.



### Termos de Responsabilidade:

Foi desenvolvido um sistema de controle de termos de responsabilidade do usuário, onde é possível criar o termo e versões do termo, para caso haja a necessidade de atualização do mesmo.

Os usuários possuem a opção de assinar o termo ou não.


### Opt-In e Opt-Out:

Cada usuário possui a opção de aceitar o Opt-In Opt-Out, e com isso, foi disponibilizada no perfil do usuário uma opção Booleana para que seja ativada essa opção ou não.

### Históricos:

Para atender as exigências da LGPD, foi desenvolvido um sistema de históricos, onde temos configurados os seguintes históricos:

* Criação de Usuário;
* Exclusão de Usuário;
* Atualização de Usuário;
* Usuários Terceiro;
* Adição de usuário terceiro em grupo de acesso;
* Remoção de usuário terceiro em grupo de acesso;
* Aceite de usuário em relação ao termo de responsabilidade;


### Cadastro de Terceiro que terão acesso à API:

Foi desenvolvido um sistema de controle de acesso à API feitas por Terceiros, onde é possível, com segurança, fornecer nossa API para clientes.

Tudo se inicia no cadastramento do terceiro, com dados de CNPJ; Razão Social e etc... Após esta etapa, é realizada a criação de um usuário do sistema, onde este será vinculado ao terceiro. 


### Autenticação utilizando Bearer Token:

Para que a API seja acessada de forma segura, foi realizada a criação de autenticação através de Bearer Token, onde o Token gerado se expira a cada 5 minutos, havendo a necessidade de um Refresh e assim continuar o acesso à API.

Esta forma de segurança é a mais utilizada no mercado. Só pelo fato da utilização do Token, já nos traz segurança, mas pelo fato de atualizar a cada 5 minutos para cada sessão, nos traz uma segurança ainda maior.

Este método é comumente indicado por equipes de segurança da informação para atender exigências da LGPD.

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

