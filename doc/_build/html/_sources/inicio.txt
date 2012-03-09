============
Para começar
============

-------------
1. Introdução
-------------
Nessa seção será mostrado as ferramentas que são pré-requisitos para desenvolvimento do projeto. Também mostraremos como instalá-las e configurá-las corretamente, para que o desenvolvedor já consiga ao menos rodar o PABX-IP em sua máquina local.

------------------------------
2. Ambiente de Desenvolvimento
------------------------------
* Sistema Operacional (recomendável): Ubuntu
* Python 2.7 (a versão 3 é incompatível com outras bibliotecas)
* Framework Django + Pinax
* Banco de dados SQLite
* Conexão com a internet

--------------------------------------------
3. Instalação do ambiente de desenvolvimento
--------------------------------------------

Esse tutorial foi feito no Ubuntu 10.04, usando o repositório git onde o código estava sendo versionado na época em que essa documentação foi feita. Caso o desenvolvedor já possua o código fonte, pule a parte 1.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.1. Instalação do git e clone do repositório:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $ sudo apt-get install git-core

    $ git clone https://github.com/fabiothiroki/pabx_ip.git


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.2. Instalação e ativação do virtualenv:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O virtualenv é uma ferramenta de criação de ambientes python isolados. Isso visa facilitar o deploy da aplicação. 

Toda vez que o desenvolvedor quiser rodar o servidor local de desenvolvimento do django é necessário ativar esse ambiente, pois é nele que estarão instalados o Pinax e as bibliotecas python auxiliares.

Antes de mais nada é interessante que todas as bibliotecas do OS sejam atualizadas

::

    $ sudo apt-get update
    $ sudo apt-get dist-update

::

    $ sudo apt-get install python-pip

    $ sudo pip install virtualenv

    $ virtualenv pabx-env

    $ source pabx-env/bin/activate

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.3. Instalação do Pinax e outros apps:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pinax é uma plataforma baseada no Django que contém diversos apps pré-instalados.

Para mais informações consulte: http://pinaxproject.com/
 
::

    (pabx-env)$ pip install Pinax 
    (pabx-env)$ pip install django_compressor
    (pabx-env)$ pip install django_debug_toolbar
    (pabx-env)$ pip install django_staticfiles
    (pabx-env)$ pip install pinax_theme_bootstrap

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.4. Instalação do Django:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Django é o framework web utilizado no projeto.

Para mais informações consulte: http://djangoproject.com/

::

    (pabx-env)$ pip install Django

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.5. Instalação do Django South:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

O South é utilizado para implementar o controle da estrutura e migração do banco de dados. Seus arquivos estão na pasta 'south', no diretório raiz do projeto.

Para mais informações consulte: http://south.aeracode.org/

::

    (pabx-env)$ pip install south

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.6. Conclusão:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Por fim utilize o seguinte comando no diretório raiz do projeto para ligar o servidor de desenvolvimento:

::

	$ python manage.py runserver

A seguinte mensagem deverá ser retornada no terminal em caso de sucesso:

::

	Validating models...

	0 errors found
	Django version 1.3.1, using settings 'pabx_ip.settings'
	Development server is running at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.

Entre com o endereço http://127.0.0.1:8000/ no seu navegador para acessar a interface web do projeto.

O banco de dados padrão do projeto vem com o usuário super-admin com login *root* e senha *1234*.