.. _smtp:

App Smtp
==============

Esse App é responsável pelo cadastro de um servidor smtp que será usado pelo PABX-IP para enviar emails diversos. A partir de um servidor smtp configurado para o PABX-IP é possível, por exemplo, mandar emails a partir de uma conta cadastrada no gmail.

Apenas um único servidor smtp é permitido, sendo que somente o Administrador pode alterar suas configurações.

Modelos
---------------------------
.. module:: smtp.server

Existe uma única classe *server* definida aqui, que corresponde aos dados do servidor smtp.

Os atributos da classe *server* são:

.. class:: server

    * **url**: url para o servidor smtp.
    * **port**: porta do servidor smtp.
    * **username**: nome de usuário do servidor smtp.
    * **password**: senha do servidor smtp.

Formulários
------------------------------
.. module:: smtp.forms

.. class:: smtpform

	Nesse *ModelForm* cujo modelo é a classe *server*, acrescentamos o campo de confirmação de senha e a validação da mesma. Esse formulário é utilizado tanto para cadastro como edição do servidor smtp.


Views
----------------

.. module:: smtp.views

.. function:: index(request)

	Função que retorna os dados do servidor smtp e imprime num template *crud*. Se o servidor não estiver configurado ainda, uma mensagem será exibida. Essa tela ainda possui links para cadastrar ou editar um servidor smtp.


.. function:: configure(request)

	Função que permite o cadastro ou a edição do servidor smtp, utilizando o *smtpform*.