from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

@given('estoy en la página de login')
def step_estoy_en_pagina_login(context):
    """Dado que estoy en la página de login"""
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login()

@when('ingreso credenciales válidas')
def step_ingreso_credenciales_validas(context):
    """Cuando ingreso credenciales válidas"""
    context.login_page.enter_username("usuario_valido")
    context.login_page.enter_password("password_valido")
    context.login_page.click_login()

@when('ingreso credenciales inválidas')
def step_ingreso_credenciales_invalidas(context):
    """Cuando ingreso credenciales inválidas"""
    context.login_page.enter_username("usuario_invalido")
    context.login_page.enter_password("password_invalido")
    context.login_page.click_login()

@then('debería ver el mensaje de bienvenida')
def step_ver_mensaje_bienvenida(context):
    """Entonces debería ver el mensaje de bienvenida"""
    assert context.login_page.is_welcome_message_visible(), "Mensaje de bienvenida no visible"

@then('debería ver un mensaje de error')
def step_ver_mensaje_error(context):
    """Entonces debería ver un mensaje de error"""
    assert context.login_page.is_error_message_visible(), "Mensaje de error no visible"