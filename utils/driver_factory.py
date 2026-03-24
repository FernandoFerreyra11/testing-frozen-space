from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

class DriverFactory:
    """Factory para crear instancias de WebDriver"""

    @staticmethod
    def create_driver(browser="chrome", headless=True):
        """
        Crear una instancia de WebDriver

        Args:
            browser (str): Navegador a usar ('chrome' o 'firefox')
            headless (bool): Ejecutar en modo headless

        Returns:
            WebDriver: Instancia del driver
        """
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

            driver_path = ChromeDriverManager().install()
            # Fix: webdriver-manager puede devolver ruta incorrecta, apuntar al .exe real
            driver_dir = os.path.dirname(driver_path)
            chromedriver_path = os.path.join(driver_dir, "chromedriver.exe")

            return webdriver.Chrome(
                service=ChromeService(chromedriver_path),
                options=options
            )

        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")

            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        else:
            raise ValueError(f"Navegador '{browser}' no soportado. Usa 'chrome' o 'firefox'.")

    @staticmethod
    def quit_driver(driver):
        """Cerrar el driver de manera segura"""
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error al cerrar el driver: {e}")