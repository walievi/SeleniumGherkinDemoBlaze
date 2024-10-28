from time import sleep
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CarrinhoPage:
    def __init__(self, driver):
        self.driver = driver

    def ir_para_pagina_carrinho(self):
        self.driver.get("https://www.demoblaze.com/cart.html")

    def clicar_botao_por_texto(self, texto):
         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{texto}']"))
         ).click()

    def preencher_dados_compra(self, nome, pais, cidade, cartao, mes, ano):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "name"))
        ).send_keys(nome)
        self.driver.find_element(By.ID, "country").send_keys(pais)
        self.driver.find_element(By.ID, "city").send_keys(cidade)
        self.driver.find_element(By.ID, "card").send_keys(cartao)
        self.driver.find_element(By.ID, "month").send_keys(mes)
        self.driver.find_element(By.ID, "year").send_keys(ano)

    def finalizar_compra(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Purchase']"))
        ).click()

    def verificar_mensagem_compra(self, texto):
        mensagem_sucesso = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//h2[text()='{texto}']"))
        )
        return mensagem_sucesso.is_displayed()

    def contar_produtos(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody[@id='tbodyid']/tr"))
        )

        tbody = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "tbodyid"))
        )
        products = tbody.find_elements(By.TAG_NAME, "tr")
        return len(products)


    def deletar(self, produto):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//tbody[@id='tbodyid']/tr[td[contains(text(), '{produto}')]]//a[text()='Delete']"))
        ).click()

    def procurar_produto(self, produto):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//tbody[@id='tbodyid']/tr[td[contains(text(), '{produto}')]]"))
            )
            sleep(2)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//tbody[@id='tbodyid']/tr[td[contains(text(), '{produto}')]]"))
            )
            return True
        except TimeoutException:
            return False

    def verificar_alerta(self, mensagem_esperada):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alerta = self.driver.switch_to.alert
            return alerta.text == mensagem_esperada
        except TimeoutException:
            return False