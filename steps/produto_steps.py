from behave import given, when
from pages.produto import ProdutoPage

@given('que o usuário esta na página de produto')
def step_visit_product_page(context):
    context.produto_page = ProdutoPage(context.driver)

@when('o usuário adiciona o produto ao carrinho')
def step_add_to_cart(context):
    context.produto_page.adicionar_ao_carrinho()

@when('confirma a mensagem de adicionado com sucesso')
def ste_confirm_alert(context):
    assert context.produto_page.verificar_alerta("Product added"), \
        "A mensagem de confirmação não foi exibida corretamente"
    context.driver.switch_to.alert.accept()