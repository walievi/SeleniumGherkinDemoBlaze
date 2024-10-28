from behave import given, when, then
from pages.home import HomePage

@given('que o usuário está na modal de contato')
def step_visit_contact_modal(context):
    context.home_page = HomePage(context.driver)
    context.home_page.ir_para_pagina_inicial()
    context.home_page.clicar_elemento_por_texto("Contact")

@when('o usuário preenche o formulário de contato')
def step_fill_contact_form(context):
    campos_formulario = {
        "recipient-email": "usuario@exemplo.com",
        "recipient-name": "Usuário de Teste",
        "message-text": "Essa é uma mensagem de teste."
    }
    context.home_page.preencher_formulario(campos_formulario)

@when('o usuário não preenche o formulário de contato')
def step_fill_empty_contact_form(context):
    campos_formulario = {
        "recipient-email": "",
        "recipient-name": "",
        "message-text": ""
    }
    context.home_page.preencher_formulario(campos_formulario)

@when('clica no botão de enviar')
def step_submit_contact_form(context):
    context.home_page.clicar_botao_por_texto("Send message")

@then('A mensagem "{mensagem}" deve ser exibida')
def step_check_error_message(context, mensagem):
    assert context.home_page.verificar_alerta(mensagem), \
        f'A mensagem "{mensagem}" não foi exibida'
    context.driver.switch_to.alert.accept()