# language: pt
Funcionalidade: Formulário de contato
    Cenário: Enviar mensagem de contato com sucesso
        Dado que o usuário está na modal de contato
        Quando o usuário preenche o formulário de contato
        E clica no botão de enviar
        Então A mensagem "Thanks for the message!!" deve ser exibida

    Cenário: Enviar mensagem de contato com erro
        Dado que o usuário está na modal de contato
        Quando o usuário não preenche o formulário de contato
        E clica no botão de enviar
        Então A mensagem "Message is empty!!" deve ser exibida
