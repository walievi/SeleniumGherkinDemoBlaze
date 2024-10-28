from behave import then

@then('o usuário deve estar desconectado')
def step_check_logout_success(context):
    context.home_page.verificar_elemento_texto("signin2", "Sign up")