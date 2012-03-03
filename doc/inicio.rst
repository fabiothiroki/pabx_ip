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
* Framework Django + Pynax
* Banco de dados SQLite

--------------------------------------------
3. Instalação do ambiente de desenvolvimento
--------------------------------------------

Esse tutorial foi feito no Ubuntu 11.10, usando o repositório git onde o código estava sendo versionado na época em que essa documentação foi feita. Caso o desenvolvedor já possua o código fonte, pule essa parte inicial.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Instalação do git e clone do repositório:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``$sudo apt-get install git``
``$git clone https://github.com/fabiothiroki/pabx_ip.git``

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2. Instalação e configuração do Pinax:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``$sudo apt-get install python-pip``
``$sudo pip install Pinax``