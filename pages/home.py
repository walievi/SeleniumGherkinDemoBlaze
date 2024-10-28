from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def ir_para_pagina_inicial(self):
        self.driver.get("https://www.demoblaze.com")

    def clicar_elemento_por_texto(self, texto):
         WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, texto))
        ).click()

    def preencher_formulario(self, campos):
        for campo, valor in campos.items():
            elemento = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.ID, campo))
            )
            elemento.send_keys(valor)

    def clicar_botao_por_texto(self, texto):
         WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{texto}']"))
         ).click()

    def verificar_alerta(self, mensagem_esperada):
        WebDriverWait(self.driver, 30).until(EC.alert_is_present())
        alerta = self.driver.switch_to.alert
        return alerta.text == mensagem_esperada

    def verificar_elemento_texto(self, elemento_id, texto_esperado):
        elemento = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, elemento_id))
        )
        assert elemento.text == texto_esperado, \
            f"O texto do elemento '{elemento_id}' não é '{texto_esperado}'"

    def click_categoria(self, categoria):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(@class, 'list-group-item') and text()='{categoria}']"))
        ).click()
        sleep(3)

    def procurar_produto(self, produto):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//div[@id='tbodyid']//a[contains(@class, 'hrefch') and text()='{produto}']"))
            )

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//div[@id='tbodyid']//a[contains(@class, 'hrefch') and text()='{produto}']"))
            )
            return True
        except:
            return False

