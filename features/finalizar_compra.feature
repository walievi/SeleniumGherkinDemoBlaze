# language: pt
Funcionalidade: Finalizar compra
	Cenário: Finalizar uma compra com sucesso
		Dado que o usuário está na página inicial
		Quando clica no menu de login
		E o usuário insere credenciais válidas
		E clica no botão de login
		Dado que o usuário está na página inicial
		Quando o usuário clica no produto "Samsung galaxy s6"
		Dado que o usuário esta na página de produto
		Quando o usuário adiciona o produto ao carrinho
		E confirma a mensagem de adicionado com sucesso
		Dado que o usuário está na página do carrinho
		Quando o usuário tem produto no carrinho
		E clica no botão de finalizar compra
		E o usuário preenche os dados de pedido
		E clica no botão comprar
		Então a compra deve ser realizada com sucesso

	Cenário: Finalizar uma compra sem Produto
		Dado que o usuário está na página inicial
		Quando clica no menu de login
		E o usuário insere credenciais válidas
		E clica no botão de login
		Dado que o usuário está na página do carrinho
		Quando clica no botão de finalizar compra
		E o usuário preenche os dados de pedido
		E clica no botão comprar
		Então deve apresentar o erro "Cannot complete purchase without products."

	Cenário: Finalizar uma compra sem preencher os dados do formulário
		Dado que o usuário está na página inicial
		Quando clica no menu de login
		E o usuário insere credenciais válidas
		E clica no botão de login
		Dado que o usuário está na página inicial
		Quando o usuário clica no produto "Samsung galaxy s6"
		Dado que o usuário esta na página de produto
		Quando o usuário adiciona o produto ao carrinho
		E confirma a mensagem de adicionado com sucesso
		Dado que o usuário está na página do carrinho
		Quando o usuário tem produto no carrinho
		E clica no botão de finalizar compra
		E clica no botão comprar
		Então deve apresentar o erro "Please fill out Name and Creditcard."
