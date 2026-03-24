from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    """Page Object para la pagina de registro"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Localizadores actualizados por el usuario (corregidos a By.ID)
        self.registrate_aqui_link = (By.ID, "auth-toggle")
        self.full_name_field = (By.ID, "auth-name")
        self.email_field = (By.ID, "auth-email")
        self.password_field = (By.ID, "auth-password")
        self.register_button = (By.ID, "auth-submit")
        self.success_message = (By.CSS_SELECTOR, "#hero > div.hero__content > h1 > span:nth-child(1)")
        self.error_message = (By.CSS_SELECTOR, "#auth-alert > div")

    def navigate_to_register(self):
        """Navegar a la pagina de registro"""
        self.driver.get("http://localhost:5173/#/register")

    def enter_email(self, email):
        """Ingresar email"""
        element = self.wait.until(EC.presence_of_element_located(self.email_field))
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        """Ingresar contraseña"""
        element = self.wait.until(EC.presence_of_element_located(self.password_field))
        element.clear()
        element.send_keys(password)

    def enter_full_name(self, name):
        """Ingresar nombre completo"""
        element = self.wait.until(EC.presence_of_element_located(self.full_name_field))
        element.clear()
        element.send_keys(name)

    def click_registrate_aqui(self):
        """Hacer clic en el link para ir al formulario de registro"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.registrate_aqui_link))
            element.click()
        except:
            pass # Si ya estamos en el form de registro, no pasa nada

    def click_register(self):
        """Hacer clic en el botón de registro"""
        element = self.wait.until(EC.element_to_be_clickable(self.register_button))
        element.click()

    def get_success_message(self):
        """Obtener el texto del mensaje de éxito"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.success_message))
            return element.text
        except:
            return ""

    def get_error_message(self):
        """Obtener el texto del mensaje de error"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            return element.text
        except:
            return ""
