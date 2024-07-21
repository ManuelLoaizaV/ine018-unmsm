import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Definamos una funcion para darnos la info de cualquiera que sea nuestra busqueda de carrera
def buscar_carrera(nombre_carrera):
    """Son opciones para configurar Chrome que es el navegador que utilice, '--start-maximized' para que 
    el navegador se abra en tamaño completo y '--disable-extensions' para quitar las extensiones"""
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    #Pasamos las opciones modificadas al webdriver base de Chrome
    driver = webdriver.Chrome(options=options)

    #Nos dirigimos a la pagina de San Marcos
    driver.get('https://unmsm.edu.pe/formacion-academica/carreras-de-pregrado')

    #Esperamos unos 10 segundos hasta que la barra cargue, si ya cargo entonces digita el nombre que ingresamos
    input_busqueda = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#input-pregrado-palabra-clave'))
        )
    input_busqueda.send_keys(nombre_carrera)

    #Deja un tiempo de 3 segundos para que aparezca la opcion especifica
    time.sleep(3)
        
    #Hacemos click en la carrera para ingresar a la info
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section[3]/div[2]/div/div/a[2]/div/p[1]/b'))
        ).click()

    #Esperamos 3 segundos para que cargue
    time.sleep(3)

    #Extraemos la informacion especifica en XPATH, personalmente utilice la opcion "inspeccionar" y busque cada opcion para que se muestre
    descripcion = driver.find_element(By.XPATH, '/html/body/main/section[2]/div[2]/div[1]/div/div[1]/p').text.strip()
    grado = driver.find_element(By.XPATH, '/html/body/main/section[2]/div[2]/div[1]/div/div[2]/p').text.strip()
    titulo = driver.find_element(By.XPATH, '/html/body/main/section[2]/div[2]/div[1]/div/div[3]/p').text.strip()
    duracion = driver.find_element(By.XPATH, '/html/body/main/section[2]/div[2]/div[1]/div/div[4]/p').text.strip()
    perfil_egresado = driver.find_element(By.XPATH, '/html/body/main/section[2]/div[2]/div[1]/div/div[5]/p').text.strip()

    #Mostramos los datos extraidos en la terminal
    print(f"Descripción: {descripcion}")
    print(f"Grado: {grado}")
    print(f"Título: {titulo}")
    print(f"Duración: {duracion}")
    print(f"Perfil del Egresado: {perfil_egresado}")

    driver.quit()

nombre_carrera = input("Ingrese el nombre de la carrera: ")
buscar_carrera(nombre_carrera)
