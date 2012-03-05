=====================
Visão geral do código
=====================

Para que o desenvolvedor não fique confuso com a quantidade de arquivos do projeto, será listado aqui os apps desenvolvidos de fato (cada app corresponde a uma pasta na raiz do projeto):

	* **Accounts**
	* **Groups**
	* **Skypelist**
	* **Smtp**

Além dos arquivos *urls.py* e *settings.py* nenhum dos outros arquivos foi codificado de fato anteriormente, mas foi gerado automaticamente pelo framework e suas ferramentas.

O código desenvolvido no projeto está seguindo a estrutura de apps do Django, assim como a documentação relativa a essa parte. 

Cada App documentado contém seu arquivos numa pasta de mesmo nome na raiz principal do projeto. Assim, a estrutura da documentação de cada app passa a ser a seguinte:

	* Formulários: relativo ao arquivo *forms.py*
	* Modelos: relativo ao arquivo *models.py*	
	* Views: relativo ao arquivo *views.py*
	* Decorators: relativo ao arquivo *decorators.py* (opcional)
	* Templates: relativo aos arquivos dentro da pasta "templates" (opcional)

Eventualmente algum App possa precisar de arquivos templates adicionais que estarão contidos na pasta "templates" dentro da pasta do App. Além desses arquivos templates, os outros templates padrão estarão contidos na pasta "templates" dentro da pasta raiz.
