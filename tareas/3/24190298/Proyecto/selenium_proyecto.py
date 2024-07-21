from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait as tiempo
from selenium.webdriver.support import expected_conditions as condicion

driver = webdriver.Chrome()
driver.get("https://unmsm.edu.pe/formacion-academica/carreras-de-pregrado")
listafinal=[]

try:
  while True:
     tiempo(driver, 60).until(
      condicion.presence_of_all_elements_located((By.XPATH, "//p[@class='mb-13px color-rojo-sm']/b"))
    )
     lista=driver.find_elements(By.XPATH, "//p[@class='mb-13px color-rojo-sm']/b")
   
     for carrera in lista:
            listafinal.append(carrera.text)
     try:
         pagina= driver.find_element(By.XPATH, "//a[@class='d-inline-block sig-paginator']")
         pagina.click()
         tiempo(driver,10).until(
          condicion.staleness_of(lista[0])
            )
     except Exception:
        print("")
        break
finally:
    driver.quit()


for carrera in listafinal:
     print(carrera)
