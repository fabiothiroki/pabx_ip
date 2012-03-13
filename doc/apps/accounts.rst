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

Views
----------------

.. module:: accounts.views

.. function:: login(request)

    View que inicialmente mostra a tela de login para o usuário, caso o usuário entre na página inicial do projeto ou tente acessar alguma outra página através da url sem estar logado. O usuário ao submeter o formulário de login através de um método POST, fará com que a view tente autenticar esse usuário, e em caso de sucesso, guardará na sessão se o usuário é admininistrador, seu username e seu id e o redirecionará para a página principal. Em caso de falha, a view retorna uma mensagem de erro para o template de login.

.. function:: logout(request)

    Faz o logout do usuário logado e o redireciona para a página de login.

.. function:: settings(request)

    É a tela que lista todos os usuários do pabx-ip e permite que o administrador escolha qual usuário editar ou remover através de uma interface. Também possui um botão para a tela de cadastro de usuários. É importante lembrar que somente o usuário 'root' pode editar ou remover outros administradores.

.. function:: create(request)

    View que usa o UserForm para cadastrar um novo usuário no sistema. Somente acessível para administradores.

.. function:: edit(request,offset)

    View que usa o UserForm para editar um usuário pré-cadastrado no sistema. Através do offset passado pela url a view sabe o id do usuário que se deseja modificar. Somente acessível para administradores. 

.. function:: delete(request)

    View usada para remover um usuário do sistema. Através do offset passado pela url a view sabe o id do usuário que se deseja deletar. Primeiramente exibe uma tela de confirmação, e em seguida caso haja confirmação por parte do administrador, a classe User e sua respectiva classe UserProfile são removidas do banco de dados.

.. function:: edit_self(request)

    View que o usa o OnlyUserForm para que um usuário comum logado para editar seu email ou senha.

.. function:: save_or_update(form,user=None,profile=None)

    Método que faz a associação entre um form e os objetos User e UserProfile. Caso os parâmetros user e profile não sejam vazios, a função interpreta como edição de usuário, e terá que fazer a busca dele no banco.

.. function:: password_reset(request)

    Retorna inicialmente o template do formulário PassResetForm onde o usuário deverá digitar um email cadastrado válido. Após a submissão do formulário, o sistema checa se existe um servidor smtp pré-cadastrado pelo administrador para envio de emails. Em caso positivo, o email é enviado, e retorna o template indicando uma mensagem de sucesso.

.. function:: encrypt(plaintext)
    
    Função que retorna a variável *plaintext* encriptada. Usada para salvar a senha encriptada dos usuários no banco.

.. function:: unencrypt(encrypted_password)

    Função que retorna a variável *encrypted_password* desencriptada. Usada para recuperar a senha dos usuários em caso de esquecimento.

Templates
----------------

Aqui serão listados os templates específicos utilizados por esse App, contidos na pasta "accounts/templates/"

    * password_reset_form.html: utilizado para renderizar o formulário para recuperação de senha.
    * password_reset_success.html: utilizado para mostrar a mensagem de sucesso na recuperação de senha.

Decorators
----------------

.. module:: accounts.decorators

.. function:: is_admin(function)
    
    Checa se o User logado possui o atributo admin na respectiva classe UserProfile. Usado para limitar o acesso a certas Views que apenas administradores podem acessar.
