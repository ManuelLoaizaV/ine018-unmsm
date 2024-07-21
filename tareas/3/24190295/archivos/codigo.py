from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#abrir paginas
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://unmsm.edu.pe/formacion-academica/carreras-de-pregrado')

#buscar las carreras
buscador = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='search']")))
buscador.clear()
buscador.send_keys("ingenieria industrial")
time.sleep(1000000)
type="search"
