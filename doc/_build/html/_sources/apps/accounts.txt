.. _accounts:

App Accounts
==============

Este app é responsável por:
    * Definir privilégios de administrador a usuários e limitar acesso a usuários comuns
    * Cadastro, edição, listagem e remoção de usuários
    * Autenticação e recuperação de senha


Modelos
---------------------------
.. module:: accounts.models

No arquivo models.py estão as classes definidas para armazenar informações extras do usuário. Podemos observar que a classe UserProfile tem uma chave estrangeira na classe User, que é a classe padrão para usuários do Django. Desta maneira, podemos extender os atributos da classe User sem alterar a estrutura de usuário do Django, bastando apenas fazer essa pequena extensão.

Os atributos definidos na classe UserProfile estão detalhados a seguir:

.. class:: UserProfile

    * **profile**: Chave estrangeira que associa um UserProfile a um Usuário. Pode haver apenas um UserProfile por User.
    * **ramal**: Ramal associado a um usuário. Esse número é utilizado para fazer ligações.
    * **passw**: É a cópia da senha do usuário salva encriptadamente. É utilizada para recuperação de senha.
    * **admin**: Indica se o usuário possui o privilégio de administrador.
    * **group**: Indica o grupo o qual o usuário pertence.

Formulários
------------------------------

.. module:: accounts.forms

.. class:: UserForm

    Formulário utilizado pelo administrador para editar ou criar usuários. Além dos campos padrões relativos a classe User e a classe UserProfile existe um *hidden input* que contém o id do usuário em caso de edição, para que possamos validar as informações na hora de salvar no banco de dados.

    O método clean é sobreescrito para validarmos a confirmação de senha e no caso de edição, temos que permitir o salvamento de um ramal ou email já existente.

.. class:: OnlyUserForm

    Formulário utilizado para que um usuário sem privilégios de administrador possa mudar seu email ou senha.

.. class:: PassResetForm

    Formulário utilizado para que um usuário possa receber sua senha esquecida no seu email. Apenas emails cadastrados são aceitos.


