# language: pt
Funcionalidade: Navegação de categoria
    Cenário: Troca de categoria
		Dado que o usuário está na página inicial
        Quando o usuário clica na categoria "Laptops"
        Então deve haver o produto "Sony vaio i5" na tela

    Cenário: Navegação em várias categorias
		Dado que o usuário está na página inicial
        Quando o usuário clica na categoria "Laptops"
        E o usuário clica na categoria "Monitors"
        Então deve haver o produto "Apple monitor 24" na tela