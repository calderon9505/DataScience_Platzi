from importlib.resources import path
import unittest
from click import UsageError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
import time

# Para que dos páginas se carguen en la misma ventana: 
# Se cambia "setUp" por "setUpClass". Igual con "teadDown".
# Se cambia "self" por "cls" 
# Se añade el decorador @classmethod a ambos métodos
# se crean los dos test con métodos por separado.

# @classmethod
# def setUpClass(cls) -> None:
#     cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                                     options=cls.options)

# @classmethod
# def tearDownClass(cls) -> None:
#     cls.driver.close()

# Para automatizar la descarga del chromedriver se Usa
# service=Service(ChromeDriverManager().install())
# Pero hace que el proceso sea más lento, porque debe realizar la descarga

class HomePageTests(unittest.TestCase):
    
    url = 'https://www.decameron.com/es/co-inicio'
    chromedriver = 'C:/Users/User/Documents/DataScience_Platzi/09_DataEngineer/WebScraping/Selenium/chromedriver.exe'

    def setUp(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--incognito')
        self.driver = webdriver.Chrome(service=Service(self.chromedriver), options=self.options)
        self.driver.get(self.url)
        self.driver.maximize_window()


    def test_box_ciudad_origen(self):
        """Finding a box"""
        box_ciudad_origen = self.driver.find_element(By.ID, 'origenCompHotel')

    def test_button_buscar(self):
        """Finding a button"""
        button_buscar = self.driver.find_element(By.ID, 'buscarHotel')

    def tearDown(self) -> None:
        self.driver.quit()




if __name__ == "__main__":
    # unittest.main(
    #               verbosity = 2,
    #               testRunner = HTMLTestRunner(output='reportes', report_name='hello-world-report')
    #              )

    unittest.main(verbosity = 2)