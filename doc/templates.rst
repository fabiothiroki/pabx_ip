=====================
Templates Padrão
=====================

Templates são usados pelo Django para exibir o conteúdo em questão para o usuário, ou seja, é o que o usuário vê de fato.

Os templates padrão são os arquivos html contidos na pasta *templates* logo na raiz do projeto. Apenas alguns arquivos dentre outros contidos nessa mesma pasta são utilizados no projeto, sendo que os não usados são arquivos criados automaticamente pelo Pinax.

Serão listados aqui os templates utilizados:

	* base.html
	* crud.html
	* form_create.html
	* form_delete.html
	* form_success.html
	* login.html
	
--------------------
base.html
--------------------

É o template base do projeto, que utiliza a mesma estrutura do *fluid layout* do Twitter bootstrap, com alguma modificação para fixar a barra superior. Aqui fica definido o *menu*, o *header* e o *footer*. O conteúdo que eventualmente será carregado na parte do meio, será parte de outro template "filho" deste.

A variável "highlight" deve ser definida em cada view para manter o link do menu destacado, na seção que o usuário estiver navegando. Assim como a variável "title" que define o valor da tag html *title*.
	
--------------------
crud.html
--------------------

Template que extende o template *base.html* e é responsável por criar as tabelas que darão acesso as operações CRUD (acrônimo de Create, Read, Update e Delete em inglês).

--------------------
form_create.html
--------------------

Template que extende o template *base.html* e é responsável por montar a estrutura dos formulários utilizados por criação e edição de dados.

Aqui também existe um script Javascript que facilita a criação do botão "cancelar", pois o link é passado pela *view* correspondente.
	
--------------------
form_delete.html
--------------------

Template que extende o template *base.html* e é responsável por montar a estrutura da tela de confirmação de remoção de algum dado.

Aqui também existe um script Javascript que facilita a criação do botão "cancelar", pois o link é passado pela *view* correspondente.

--------------------
form_success.html
--------------------

Template que extende o template *base.html* e é responsável por montar a estrutura da tela de sucesso no caso de alguma ação (criação,edição ou remoção) ter sido executada com sucesso.

Aqui também existe um script Javascript que facilita a criação do botão "voltar", pois o link é passado pela *view* correspondente.

--------------------
login.html
--------------------

Template que é responsável por montar o formulário de login do usuário.