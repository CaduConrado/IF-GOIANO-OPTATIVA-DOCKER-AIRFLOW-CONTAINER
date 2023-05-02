from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Principal (webdriver.Chrome): 
    def __init__(self): 
        options = webdriver.ChromeOptions().add_experimental_option \
            ('excludeSwitches', ['enable-logging'])
        service = Service(ChromeDriverManager().install())
        super(Principal, self).__init__(service=service, options=options)
        self.maximize_window()

    def abrirFace(self):
        self.get('https://www.facebook.com')
        print('O Título da página é: ', self.title)
        print('O endereço url é: ', self.current_url)
        time.sleep(10)

    def pesquisa_google(self):
        self.get('https://www.google.com')
        campo_busca = self.find_element(By.CSS_SELECTOR, \
                                        'textarea[title="Pesquisar"]')
        campo_busca.send_keys('Automação de processos')
        campo_busca.submit()
    
    def loginGuru(self):
        self.get('https://www.demo.guru99.com/test/newtours')
        usuario = self.find_element(By.NAME, "userName")
        senha = self.find_element(By.NAME, "password")
        submit = self.find_element(By.NAME, "submit")
        usuario.send_keys('mercury')
        senha.send_keys('mercury')
        submit.click()
        time.sleep(3)

if __name__ == "__main__":
    bot = Principal()
    bot.loginGuru()

