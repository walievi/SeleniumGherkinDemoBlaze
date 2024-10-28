# language: pt
Funcionalidade: Logout do usuário
	Cenário: Realizar logout com sucesso
		Dado que o usuário está na página inicial
		Quando clica no menu de login
		E o usuário insere credenciais válidas
		E clica no botão de login
		E clica no botão de logout
		Então o usuário deve estar desconectado