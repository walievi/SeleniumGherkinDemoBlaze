from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProdutoPage:
    def __init__(self, driver):
        self.driver = driver

    def adicionar_ao_carrinho(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
        ).click()

    def verificar_alerta(self, mensagem_esperada):
        WebDriverWait(self.driver, 30).until(EC.alert_is_present())
        alerta = self.driver.switch_to.alert
        return alerta.text == mensagem_esperada