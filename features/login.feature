# language: pt
Funcionalidade: Login de usuário
	Cenário: Realizar login com sucesso
		Dado que o usuário está na página inicial
		Quando clica no menu de login
		E o usuário insere credenciais válidas
		E clica no botão de login
		Então o login deve ser realizado com sucesso

	Cenário: Realizar login com erro
		Dado que o usuário está na página inicial
		Quando clica no menu de login
		E o usuário insere credenciais inválidas
		E clica no botão de login
		Então o login deve apresentar mensagem de erro