from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def get_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--headless')
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
