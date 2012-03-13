.. _skypelist:

App Skypelist
==============

Esse app é responsável por:
	* Criar, editar e remover contatos skype

Um contato Skype é apenas uma associação entre um nome de usuário Skype pré-cadastrado e um ramal do pabx, sendo que este ramal deve ser único, independente de ser um ramal normal ou "skype". A idéia por trás disso está em possibilitar o usuário a fazer ligações skype de um telefone normal, conectado ao PABX-IP. 

Todas essas funcionalidades desse App está apenas acessível para Administradores.

Modelos
---------------------------
.. module:: skypelist.skypeuser

Existe uma uńica classe *skypeuser* definida aqui, que corresponde a associação entre nome de usuário skype e ramal.

Os atributos da classe *skypeuser* são:

.. class:: skypeuser

    * **ramal**: número do ramal.
    * **username**: nome de usuário Skype.

Formulários
------------------------------
.. module:: skypelist.forms

.. class:: skypeform

	*ModelForm* que utiliza como modelo a classe *skypeuser*. Acrescenta um campo *hidden input* para tratar o caso de edição do usuário, para evitar a validação de campos com mesmos valores.

Views
----------------

.. module:: skypelist.views

.. function:: index(request)

	Função que retorna a lista com os usuários skype cadastrados, utilizando o template *crud*. Esse template possui links para edição, remoção e criação.

.. function:: create(request)

	View que utiliza o *skypeform* para criar novos usuários skype.


.. function:: edit(request,offset)

	View que utiliza o *skypeform* para editar usuários skype pré-cadastrados. Através do offset passado pela url a view sabe o id do usuário skype que se deseja modificar.

.. function::  delete(request,offset):

	 View usada para remover um usuário skype do sistema. Através do offset passado pela url a view sabe o id do usuário skype que se deseja deletar.Primeiramente exibe uma tela de confirmação, e em seguida caso haja confirmação por parte do administrador, a classe *skypuser* é removida do banco de dados.