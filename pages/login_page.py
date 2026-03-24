from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object para la pagina de login"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Localizadores
        self.username_field = (By.ID, "auth-email")
        self.password_field = (By.ID, "auth-password")
        self.login_button = (By.ID, "auth-submit")
        self.welcome_message = (By.CSS_SELECTOR, "#hero > div.hero__content > h1 > span:nth-child(1)")
        self.error_message = (By.ID, "error-message")

    def navigate_to_login(self):
        """Navegar a la pagina de login"""
        self.driver.get("http://localhost:5173/#/login")  # Cambia por tu URL real

    def enter_username(self, username):
        """Ingresar nombre de usuario"""
        element = self.wait.until(EC.presence_of_element_located(self.username_field))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        """Ingresar contraseña"""
        element = self.wait.until(EC.presence_of_element_located(self.password_field))
        element.clear()
        element.send_keys(password)

    def click_login(self):
        """Hacer clic en el botón de login"""
        element = self.wait.until(EC.element_to_be_clickable(self.login_button))
        element.click()

    def is_welcome_message_visible(self):
        """Verificar si el mensaje de bienvenida es visible"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.welcome_message))
            return element.is_displayed()
        except:
            return False

    def is_error_message_visible(self):
        """Verificar si el mensaje de error es visible"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            return element.is_displayed()
        except:
            return False

    def get_error_message(self):
        """Obtener el texto del mensaje de error"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            return element.text
        except:
            return ""