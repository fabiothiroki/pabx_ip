.. _groups:

App Groups
==============

Este app é responsável por:
    * Criar, editar e excluir grupos
    * Associar permissões de usuários a um ou mais grupos

Todas as funcionalidades de grupos é apenas acessível para administradores.

.. warning::
    
    Esse App não foi finalizado ainda, portanto não atende ainda a todos os requisitos atuais do projeto. Porém no estágio em que ele está desenvolvido é possível rodar o App com as funcionalidades atuais sem problemas.
    
Modelos
---------------------------
.. module:: groups.models

Existe uma única classe *Group* definida aqui, que corresponde obviamente a um grupo. Um uso prático para essa classe é poder separar grupos de usuários por departamento, por exemplo: "grupo recepção" e "grupo gerência".

A associação entre grupos e usuários está definida no model *UserProfile* no qual o atributo *group* define o grupo do usuário. Portanto, um grupo possui vários usuários, mas um usuário só pode se associar a um grupo.

Os atributos da classe grupo são:

.. class:: Group

    * **name**: nome do grupo, usado apenas para identificá-lo.
    * **can_call_ramal**: permissão dada como padrão para todos os grupos, mantemos aqui apenas para fins de visualização.
    * **can_call_emergency**: permissão dada como padrão para todos os grupos, mantemos aqui apenas para fins de visualização.
    * **can_call_fix**: indica se o grupo pode fazer ligações para fixo local.
    * **can_call_mobile**: indica se o grupo pode fazer ligações para celular local.
    * **can_call_ddd**: indica se grupo pode fazer ligações DDD.
    * **can_call_ddi**: indica se grupo pode fazer ligações DDI.
    * **can_call_0800**: indica se grupo pode fazer ligações 0800.
    * **can_call_0300**: indica se grupo pode fazer ligações 0300.
    
    A função *unicode* serve para retornar o nome do grupo no caso de imprimirmos algum objeto Group.

Formulários
------------------------------
.. module:: groups.forms

.. class:: GroupForm

    *ModelForm* que utiliza como modelo a classe *Group*. A partir dele é possível criar ou editar grupos, e a única instância feita por essa classe é desabilitar o checkbox de permissão para ligar para ramal e para emergência, pois estas permissões são dadas como padrão para qualquer grupo.

Views
----------------

.. module:: groups.views

.. function:: index(request)

    Função que retorna a lista com os grupos cadastrados, utilizando o template *crud*. Esse template possui links para edição, remoção e criação de grupos.

.. function:: create(request)

    View que utiliza o *GroupForm* para criar novos grupos.



    

