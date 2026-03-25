import os
import csv
import platform
from datetime import datetime
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

    # Iniciar reporte de resultados
    context.test_results = []


def after_all(context):
    """Teardown que se ejecuta despues de todas las pruebas"""
    if hasattr(context, 'driver'):
        context.driver.quit()

    # Guardar reporte CSV
    if hasattr(context, 'test_results'):
        csv_report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reporte.csv")
        with open(csv_report_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Hora de Ejecucion", "Escenario", "Estado", "Duracion (s)", "Infraestructura", "Mensaje de Error"])
            for res in context.test_results:
                writer.writerow(res)

def before_scenario(context, scenario):
    """Setup que se ejecuta antes de cada escenario"""
    # Aqui puedes agregar configuracion especifica por escenario
    pass

def after_scenario(context, scenario):
    """Teardown que se ejecuta despues de cada escenario"""
    if hasattr(context, 'test_results'):
        duration = round(scenario.duration, 2) if hasattr(scenario, 'duration') else 0
        
        # Hora de ejecución
        run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Mensaje de error (si falló)
        error_msg = ""
        if scenario.status.name == 'failed' and getattr(scenario, 'error_message', None):
            # Limpiamos los saltos de línea para que no rompa la estructura del CSV
            raw_error = str(scenario.error_message).split('\n')
            error_msg = ' '.join(raw_error[:2]) # Tomamos solo las primeras lineas relevantes

        # Infraestructura
        infra = f"{platform.system()} {platform.release()}"
        if hasattr(context, 'driver') and context.driver:
            try:
                browser = context.driver.capabilities.get('browserName', 'Chrome')
                version = context.driver.capabilities.get('browserVersion', '?')
                infra += f" | {browser.capitalize()} {version}"
            except Exception:
                pass

        context.test_results.append([run_time, scenario.name, scenario.status.name, duration, infra, error_msg])