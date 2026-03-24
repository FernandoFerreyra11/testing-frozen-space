import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from utils.csv_utils import read_users_csv


def before_all(context):
    """Setup que se ejecuta antes de todas las pruebas"""
    # Configurar WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Descomenta para ejecutar sin interfaz gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver_path = ChromeDriverManager().install()
    # Fix: webdriver-manager puede devolver ruta incorrecta, apuntar al .exe real
    driver_dir = os.path.dirname(driver_path)
    chromedriver_path = os.path.join(driver_dir, "chromedriver.exe")
    
    context.driver = webdriver.Chrome(
        service=ChromeService(chromedriver_path),
        options=options
    )
    context.driver.implicitly_wait(20)
    context.driver.maximize_window()

    # Leer credenciales desde CSV
    csv_path = os.path.join(os.path.dirname(__file__), "users.csv")
    context.users = read_users_csv(csv_path)

    invalid_csv_path = os.path.join(os.path.dirname(__file__), "invalid_users.csv")
    context.invalid_users = read_users_csv(invalid_csv_path)

    register_csv_path = os.path.join(os.path.dirname(__file__), "register_users.csv")
    context.register_users = read_users_csv(register_csv_path)


def after_all(context):
    """Teardown que se ejecuta despues de todas las pruebas"""
    if hasattr(context, 'driver'):
        context.driver.quit()

def before_scenario(context, scenario):
    """Setup que se ejecuta antes de cada escenario"""
    # Aqui puedes agregar configuracion especifica por escenario
    pass

def after_scenario(context, scenario):
    """Teardown que se ejecuta despues de cada escenario"""
    # Aqui puedes agregar limpieza especifica por escenario
    pass