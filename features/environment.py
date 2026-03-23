from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def before_all(context):
    """Setup que se ejecuta antes de todas las pruebas"""
    # Configurar WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    context.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

def after_all(context):
    """Teardown que se ejecuta después de todas las pruebas"""
    if hasattr(context, 'driver'):
        context.driver.quit()

def before_scenario(context, scenario):
    """Setup que se ejecuta antes de cada escenario"""
    # Aquí puedes agregar configuración específica por escenario
    pass

def after_scenario(context, scenario):
    """Teardown que se ejecuta después de cada escenario"""
    # Aquí puedes agregar limpieza específica por escenario
    pass