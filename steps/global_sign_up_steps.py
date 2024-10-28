import random
import string
from behave import when, then

@when('o usuário insere credenciais válidas para um nova conta')
def step_fill_signup_form(context):
    campos_formulario = {
        "sign-username": ''.join(random.choices(string.ascii_letters + string.digits, k=30)),
        "sign-password": "admin"
    }
    context.home_page.preencher_formulario(campos_formulario)

@when("o usuário insere apenas username nas credenciais para um nova conta")
def step_fill_signup_form(context):
    campos_formulario = {
        "sign-username": ''.join(random.choices(string.ascii_letters + string.digits, k=30)),
        "sign-password": ""
    }
    context.home_page.preencher_formulario(campos_formulario)

@when('o usuário insere credenciais já cadastradas')
def step_fill_signup_form(context):
    campos_formulario = {
        "sign-username": 'admin',
        "sign-password": "admin"
    }
    context.home_page.preencher_formulario(campos_formulario)

@when('clica no botão de criar')
def step_submit_login_form(context):
    context.home_page.clicar_botao_por_texto("Sign up")

@then('o usuário deve ser criado com sucesso')
def step_check_signup_success(context):
    assert context.home_page.verificar_alerta("Sign up successful."), \
        "O usuário não foi criado com sucesso"


@then('deve apresentar o erro "{erro}" ao criar')
def step_check_erro(context, erro):
    assert context.home_page.verificar_alerta(erro), \
        f'A mensagem "{erro}" não foi exibida'
    context.driver.switch_to.alert.accept()