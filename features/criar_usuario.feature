# language: pt
Funcionalidade: criação de usuário
	Cenário: Criar um usuário novo
		Dado que o usuário está na página inicial
		Quando clica no menu do sign up
		E o usuário insere credenciais válidas para um nova conta
		E clica no botão de criar
		Então o usuário deve ser criado com sucesso

	Cenário: Tentar criar um usuário que já existe
		Dado que o usuário está na página inicial
		Quando clica no menu do sign up
		E o usuário insere credenciais já cadastradas
		E clica no botão de criar
		Então deve apresentar o erro "This user already exist." ao criar

	Cenário: Tentar criar um usuário sem senha
		Dado que o usuário está na página inicial
		Quando clica no menu do sign up
		E o usuário insere apenas username nas credenciais para um nova conta
		E clica no botão de criar
		Então deve apresentar o erro "Please fill out Username and Password." ao criar
