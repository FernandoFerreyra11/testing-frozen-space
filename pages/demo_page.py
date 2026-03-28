from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoPage:
    """Page Object para la seccion de Solicitud de Demo (en Home)"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Localizadores basados en home.js
        self.contact_section = (By.ID, "contact")
        self.demo_form = (By.ID, "demo-form")
        self.name_field = (By.NAME, "name")
        self.email_field = (By.NAME, "email")
        self.company_field = (By.NAME, "company")
        self.role_field = (By.NAME, "role")
        self.submit_button = (By.CSS_SELECTOR, "#demo-form button[type='submit']")

    def navigate_to_demo(self, email=None, password=None):
        """Navega a la seccion de contacto, logueandose si es necesario"""
        self.driver.get("http://localhost:5173/#/home")
        
        # Si redirige a login, procedemos a autenticarnos
        if "login" in self.driver.current_url:
            from pages.login_page import LoginPage
            login = LoginPage(self.driver)
            login.enter_username(email or "feliguerrero@frozenspace.com")
            login.enter_password(password or "testing123")
            login.click_login()
            # Esperar a volver a home
            self.wait.until(EC.url_contains("#/home"))

        # Desplazarse a la sección de contacto
        section = self.wait.until(EC.presence_of_element_located(self.contact_section))
        self.driver.execute_script("arguments[0].scrollIntoView();", section)

    def enter_name(self, name):
        element = self.wait.until(EC.presence_of_element_located(self.name_field))
        element.clear()
        element.send_keys(name)

    def enter_email(self, email):
        element = self.wait.until(EC.presence_of_element_located(self.email_field))
        element.clear()
        element.send_keys(email)

    def enter_company(self, company):
        element = self.wait.until(EC.presence_of_element_located(self.company_field))
        element.clear()
        element.send_keys(company)

    def enter_role(self, role):
        element = self.wait.until(EC.presence_of_element_located(self.role_field))
        element.clear()
        element.send_keys(role)

    def click_submit(self):
        element = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        element.click()

    def get_validation_message(self, field_name):
        """Obtiene el mensaje de validacion nativo de HTML5"""
        field_map = {
            "name": self.name_field,
            "email": self.email_field,
            "company": self.company_field,
            "role": self.role_field
        }
        element = self.driver.find_element(*field_map[field_name])
        return element.get_attribute("validationMessage")

    def handle_alert(self):
        """Maneja la alerta de exito o error y devuelve su texto"""
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return None
