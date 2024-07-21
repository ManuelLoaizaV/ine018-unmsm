from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome (
  service = Service(ChromeDriverManager().install())
)

driver.get('https://unmsm.edu.pe/formacion-academica/carreras-de-pregrado')

sleep(3)

carreras_list = []

for i in range(9): #9 es el numero de paginas de sm

  carreras = driver.find_elements(By.XPATH, '//p[@class="mb-13px color-rojo-sm"]')
  for carrera in carreras:
      carreras_list.append(carrera.text)
  sleep(2)
  
  next = driver.find_element(By.XPATH, '//a[@class="d-inline-block sig-paginator"]')
  next.click()
  sleep(1)

sleep(1)
final = '\n'.join(carreras_list)

with open('output.txt', 'w') as file:
   file.write(final)