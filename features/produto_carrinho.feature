# language: pt
Funcionalidade: Carrinho de produtos
    Cenário: Adicionar o produto ao carrinho
		Dado que o usuário está na página inicial
		Quando o usuário clica no produto "Samsung galaxy s6"
		Dado que o usuário esta na página de produto
		Quando o usuário adiciona o produto ao carrinho
        E confirma a mensagem de adicionado com sucesso
        Dado que o usuário está na página do carrinho
        Então deve haver produtos no carrinho

    Cenário: Remover Produto do Carrinho
		Dado que o usuário está na página inicial
		Quando o usuário clica no produto "Samsung galaxy s6"
		Dado que o usuário esta na página de produto
		Quando o usuário adiciona o produto ao carrinho
        E confirma a mensagem de adicionado com sucesso
        Dado que o usuário está na página do carrinho
        Quando clicar no botão de deletar do produto "Samsung galaxy s6"
		Então não deve haver o produto "Samsung galaxy s6" no carrinho