=====================
Visão geral do código
=====================

A linguagem escolhida (Python) para o desenvolvimento do projeto prioriza a legibilidade do código sobre a velocidade, bem como o framework Django. Assim, um desenvolvedor com uma certa experiência em Python não terá maiores problemas para entender o código, mesmo porque o mesmo se encontra num estágio inicial.

Ainda sim esse documento visa explicar o código mais detalhadamente e ao mesmo tempo dando alguma noção de Django.

Além dos arquivos *urls.py* e *settings.py* nenhum dos outros arquivos na pasta raiz do projeto foi codificado de fato anteriormente, mas foi gerado automaticamente pelo framework e suas ferramentas.

Os outros arquivos codificados se encontram dentro das pastas dos respectivos Apps, que serão explicados abaixo.

--------------
Apps do Django
--------------

Os apps desenvolvidos anteriormente foram (cada app corresponde a uma pasta na raiz do projeto):

	* **Accounts**
	* **Groups**
	* **Skypelist**
	* **Smtp**

Cada App do Django corresponde a um objeto assim como na programação orientada a objetos, então cada um deles possui métodos e atributos próprios seguindo uma arquitetura de software MVC adaptada.

O código desenvolvido no projeto está seguindo a estrutura de apps do Django, assim como a documentação relativa a essa parte. 

Cada App documentado contém seu arquivos numa pasta de mesmo nome na raiz principal do projeto. Assim, a estrutura da documentação de cada app passa a ser a seguinte:

^^^^^^^^^^^^^^^
Formulários 
^^^^^^^^^^^^^^^

Relativo ao arquivo *forms.py*, é responsável por criar as classes de formulários, indicando quais campos devem ser incluídos e sua validação. É um arquivo opcional, ou seja, ele existirá somente se o App precisar.

^^^^^^^^^^^^^^^
Modelos 
^^^^^^^^^^^^^^^

Relativo ao arquivo *models.py*, é justamente o *Model* da arquitetura MVC.

^^^^^^^^^^^^^^^
Views
^^^^^^^^^^^^^^^
 
Relativo ao arquivo *views.py*. Embora o nome seja confuso esse arquivo é mais parecido com o *Controller* da arquitetura MVC.

É reponsável por:

    * Toda lógica de negócios (direta ou indireta)
    * Atribuir variáveis a serem exibidas num *template*
    * Fazer chamadas ao banco de dados

^^^^^^^^^^^^^^^
Decorators
^^^^^^^^^^^^^^^

Relativo ao arquivo *decorators.py*. Aqui são declaradas algumas funções de uso geral que são chamadas diversas vezes nas views. É um arquivo opcional, ou seja, ele existirá somente se o App precisar.

^^^^^^^^^^^^^^^
Templates
^^^^^^^^^^^^^^^

Relativo aos arquivos dentro da pasta "templates". Embora o nome seja confuso esse arquivo é mais pareciso com a *View* da arquitetura MVC, pois é aqui onde a interface do usuário é renderizada a partir de elementos construídos no arquivo *views.py*

Eventualmente algum App possa precisar de arquivos templates adicionais que estarão contidos na pasta "templates" dentro da pasta do App. Além desses arquivos templates, os outros templates padrão estarão contidos na pasta "templates" dentro da pasta raiz.

-------------------------
Integração com o Asterisk
-------------------------

Por enquanto a aplicação web do PABX-IP não está integrado com o Asterisk (o software responsável pelo PBX). Para isso seria necessário escrever os dados necessários nos arquivos de configurações utilizados pelo Asterisk, usando sua própria sintaxe.

A integração entre a aplicação web e o Asterisk foi pensada da seguinte forma:

	* Todas as configurações seriam salvas no banco de dados da aplicação web, evitando assim de ter que "carregar" essas configurações a partir do Asterisk toda vez que a aplicação web fosse acessada.
	* Qualquer alteraçao dessas configurações seria primeiramente salva no banco de dados e em seguida encaminhada para o Asterisk.


