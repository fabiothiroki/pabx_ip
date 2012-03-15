=====================
Templates Padr�o
=====================

Templates s�o usados pelo Django para exibir o conte�do em quest�o para o usu�rio, ou seja, � o que o usu�rio v� de fato.

Os templates padr�o s�o os arquivos html contidos na pasta *templates* logo na raiz do projeto. Apenas alguns arquivos dentre outros contidos nessa mesma pasta s�o utilizados no projeto, sendo que os n�o usados s�o arquivos criados automaticamente pelo Pinax.

Ser�o listados aqui os templates utilizados:

	* base.html
	* crud.html
	* form_create.html
	* form_delete.html
	* form_success.html
	* login.html
	
--------------------
base.html
--------------------

� o template base do projeto, que utiliza a mesma estrutura do *fluid layout* do Twitter bootstrap, com alguma modifica��o para fixar a barra superior. Aqui fica definido o *menu*, o *header* e o *footer*. O conte�do que eventualmente ser� carregado na parte do meio, ser� parte de outro template "filho" deste.

A vari�vel "highlight" deve ser definida em cada view para manter o link do menu destacado, na se��o que o usu�rio estiver navegando. Assim como a vari�vel "title" que define o valor da tag html *title*.
	
--------------------
crud.html
--------------------

Template que extende o template *base.html* e � respons�vel por criar as tabelas que dar�o acesso as opera��es CRUD (acr�nimo de Create, Read, Update e Delete em ingl�s).

--------------------
form_create.html
--------------------

Template que extende o template *base.html* e � respons�vel por montar a estrutura dos formul�rios utilizados por cria��o e edi��o de dados.

Aqui tamb�m existe um script Javascript que facilita a cria��o do bot�o "cancelar", pois o link � passado pela *view* correspondente.
	
--------------------
form_delete.html
--------------------

Template que extende o template *base.html* e � respons�vel por montar a estrutura da tela de confirma��o de remo��o de algum dado.

Aqui tamb�m existe um script Javascript que facilita a cria��o do bot�o "cancelar", pois o link � passado pela *view* correspondente.

--------------------
form_success.html
--------------------

Template que extende o template *base.html* e � respons�vel por montar a estrutura da tela de sucesso no caso de alguma a��o (cria��o,edi��o ou remo��o) ter sido executada com sucesso.

Aqui tamb�m existe um script Javascript que facilita a cria��o do bot�o "voltar", pois o link � passado pela *view* correspondente.

--------------------
login.html
--------------------

Template que � respons�vel por montar o formul�rio de login do usu�rio.