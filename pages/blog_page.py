from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BlogPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost:5173/#/blog" # Ajustado para puerto Vite
        
        # Locators
        self.title_input = (By.ID, "blog-title")
        self.content_textarea = (By.ID, "blog-content")
        self.image_1_input = (By.ID, "blog-image-1")
        self.image_2_input = (By.ID, "blog-image-2")
        self.publish_button = (By.ID, "btn-publish")
        self.posts_container = (By.ID, "blog-posts")
        self.char_count = (By.ID, "char-count")
        
    def navigate_to_blog(self):
        self.driver.get(self.url)
        # Esperar a que el contenedor cargue
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.posts_container)
        )

    def enter_title(self, title):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.title_input))
        element.clear()
        element.send_keys(title)

    def enter_content(self, content):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.content_textarea))
        element.clear()
        element.send_keys(content)

    def enter_image_1(self, url):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.image_1_input))
        element.clear()
        element.send_keys(url)

    def enter_image_2(self, url):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.image_2_input))
        element.clear()
        element.send_keys(url)

    def click_publish(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.publish_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        import time
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

    def is_post_visible(self, title):
        try:
            xpath = f"//h3[contains(text(), '{title}')]"
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False

    def is_publish_button_enabled(self):
        element = self.driver.find_element(*self.publish_button)
        return element.is_enabled()

    def get_char_count_text(self):
        element = self.driver.find_element(*self.char_count)
        return element.text
