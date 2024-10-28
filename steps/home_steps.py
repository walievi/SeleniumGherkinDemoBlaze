from behave import given, when, then
from pages.home import HomePage

@given('que o usuário está na página inicial')
def step_visit_login_modal(context):
    context.home_page = HomePage(context.driver)
    context.home_page.ir_para_pagina_inicial()

@when('clica no menu de login')
def step_click_login_menu(context):
    context.home_page.clicar_elemento_por_texto("Log in")

@when('clica no botão de logout')
def step_click_logout_menu(context):
    context.home_page.clicar_elemento_por_texto("Log out")

@when('clica no menu do carrinho')
def step_click_logout_menu(context):
    context.home_page.clicar_elemento_por_texto("Cart")

@when('clica no menu do sign up')
def step_click_logout_menu(context):
    context.home_page.clicar_elemento_por_texto("Sign up")

@when('o usuário clica no produto "{produto}"')
def step_click_product(context, produto):
    context.home_page.clicar_elemento_por_texto(produto)

@when('o usuário clica na categoria "{categoria}"')
def step_click_category(context, categoria):
    context.home_page.click_categoria(categoria)

@then('deve haver o produto "{produto}" na tela')
def step_check_product(context, produto):
    assert context.home_page.procurar_produto(produto), f"O produto {produto} não está na tela"
