from behave import given, when, then
from pages.carrinho import CarrinhoPage

@given('que o usuário está na página do carrinho')
def step_visit_cart_page(context):
    context.carrinho_page = CarrinhoPage(context.driver)
    context.carrinho_page.ir_para_pagina_carrinho()

@when('o usuário tem produto no carrinho')
@then('deve haver produtos no carrinho')
def step_cart_not_empty(context):
    linhas_tbody = context.carrinho_page.contar_produtos()
    assert linhas_tbody > 0, "O carrinho está vazio"

@when('clica no botão de finalizar compra')
def step_click_checkout_button(context):
    context.carrinho_page.clicar_botao_por_texto("Place Order")

@when('o usuário preenche os dados de pedido')
def step_fill_order_data(context):
    context.carrinho_page.preencher_dados_compra("João da Silva", "Brasil", "Novo Hamburgo", 1234123412341234, 1, 2030)

@when('clica no botão comprar')
def step_click_buy_button(context):
    context.carrinho_page.clicar_botao_por_texto("Purchase")

@then('a compra deve ser realizada com sucesso')
def step_check_purchase(context):
    assert context.carrinho_page.verificar_mensagem_compra('Thank you for your purchase!'), "A compra não foi realizada com sucesso"

@when('clicar no botão de deletar do produto "{produto}"')
def step_click_delete_button(context, produto):
    context.carrinho_page.deletar(produto)

@then('não deve haver o produto "{produto}" no carrinho')
def step_check_cart(context, produto):
    assert not context.carrinho_page.procurar_produto(produto), f"O produto {produto} ainda está no carrinho"

@then('deve apresentar o erro "{erro}"')
def step_check_purchase(context, erro):
    assert context.carrinho_page.verificar_alerta(erro), f"Não apresentou a mensagem {erro}"