from behave import when, then

@when('o usuário insere credenciais válidas')
def step_fill_login_form(context):
    campos_formulario = {
        "loginusername": "admin",
        "loginpassword": "admin",
    }
    context.home_page.preencher_formulario(campos_formulario)

@when('o usuário insere credenciais inválidas')
def step_fill_login_form(context):
    campos_formulario = {
        "loginusername": "umUsuárioQueSabemosQueNãoExiste",
        "loginpassword": "eASenhaTambémNãoExiste",
    }
    context.home_page.preencher_formulario(campos_formulario)

@when('clica no botão de login')
def step_submit_login_form(context):
    context.home_page.clicar_botao_por_texto("Log in")

@then('o login deve ser realizado com sucesso')
def step_check_login(context):
    context.home_page.verificar_elemento_texto("nameofuser", "Welcome admin")

@then('o login deve apresentar mensagem de erro')
def step_check_login_erro(context):
    assert context.home_page.verificar_alerta("User does not exist."), \
        "A mensagem de erro não foi exibida corretamente"
    context.driver.switch_to.alert.accept()