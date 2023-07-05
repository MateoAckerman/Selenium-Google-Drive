from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import pyautogui

# from pywinauto import Desktop, Application

mail_address = "jose-antonio.mateo-lara.external@airbus.com"


# Ruta de la carpeta que deseas subir
carpeta = r"C:\Users\JMATM96M\Desktop\Selenium\uploadTest"

# Ruta del archivo chromedriver.exe
driver_path = r"C:\Users\JMATM96M\Desktop\Selenium\ChromeDriver\chromedriver.exe"

# Inicializar el navegador Chrome
driver = webdriver.Chrome()

# Iniciar sesión en Google Drive
driver.get("https://drive.google.com/drive/folders")
# time.sleep(4)  # Esperar a que la página se cargue completamente

# Rellenar el campo de correo electrónico/usuario
# Esperar a que la página se cargue después de enviar el correo electrónico
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
)

email_input.send_keys(mail_address)
email_input.send_keys(Keys.RETURN)

time.sleep(5)  # Esperar a que la página se cargue después de enviar la contraseña

# Rellenar el campo de contraseña si hubiera
# password_input = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "password"))
# )
# password_input.send_keys("04+Ackerman+23.0")
# password_input.send_keys(Keys.RETURN)

nextButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "button"))
)
nextButton.click()
# next = driver.find_element(
#     By.TAG_NAME,
#     "button",
# )

time.sleep(5)  # Esperar a que la página se cargue después de enviar la contraseña

# Verificar si se ha iniciado sesión correctamente
logged_in = False
if "accounts.google.com/ServiceLogin" not in driver.current_url:
    logged_in = True

# Navegar a la ubicación donde deseas subir la carpeta
driver.get("https://drive.google.com/drive/folders/1uBXD7jK3IL4M2BbEV8-8QrX2wEJ9dGQ1")
time.sleep(4)

# Continuar con el proceso de subida de archivos si se ha iniciado sesión correctamente
if logged_in:
    # Subir cada archivo de la carpeta
    files = os.listdir(carpeta)
    for file_name in files:
        file_path = os.path.join(carpeta, file_name)
        print("Esto es el path del archivo." + file_path)

        # Hacer clic en el botón "Nuevo" y seleccionar "Subir archivo"
        # nuevo_btn = driver.find_element_by_css_selector("a-ec-Gd a-ec-Gd-Cs-mp-S")
        new_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="drive_main_page"]/div/div[4]/div/button[1]')
            )
        )
        # nuevo_btn = driver.find_element(
        #     By.XPATH, '//*[@id="drive_main_page"]/div/div[4]/div/button[1]'
        # )
        new_btn.click()
        # time.sleep(5)

        upload_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[aria-label='Subir archivo']")
            )
        )
        upload_btn.click()

        # subir_archivo_btn = driver.find_element(
        #     By.CSS_SELECTOR, "div[aria-label='Subir archivo']"

        # )
        time.sleep(5)

        # Enviar la ruta del archivo al cuadro de diálogo de selección de archivo
        # file_input = driver.switch_to.active_element
        # file_input = driver.switch_to.alert
        # file_input.send_keys(file_path)
        # time.sleep(4)
        # file_input.send_keys(Keys.RETURN)

        # # Esperar a que el archivo se suba

        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(5)
# Cerrar el navegador
driver.quit()
