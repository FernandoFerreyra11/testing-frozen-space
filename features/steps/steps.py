from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.csv_utils import get_user_by_index


@given('estoy en la pagina de login')
def step_estoy_en_pagina_login(context):
    """Dado que estoy en la pagina de login"""
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login()


@when('ingreso credenciales validas')
def step_ingreso_credenciales_validas(context):
    """Cuando ingreso credenciales validas (primera fila CSV)"""
    if not context.users:
        raise ValueError("No hay usuarios cargados desde CSV")

    user = context.users[0]
    context.login_page.enter_username(user.get("email") or user.get("username"))
    context.login_page.enter_password(user.get("password"))
    context.login_page.click_login()


@when('ingreso credenciales invalidas')
def step_ingreso_credenciales_invalidas(context):
    """Cuando ingreso credenciales invalidas"""
    context.login_page.enter_username("no_existe@frozenspace.com")
    context.login_page.enter_password("password_invalido")
    context.login_page.click_login()


@when('ingreso credenciales desde CSV con indice {index:d}')
def step_ingreso_credenciales_csv(context, index):
    """Cuando ingreso credenciales desde CSV con un indice especifico Ratio"""
    user = get_user_by_index(context.users, index)
    context.login_page.enter_username(user.get("email") or user.get("username"))
    context.login_page.enter_password(user.get("password"))
    context.login_page.click_login()


@when('ingreso credenciales invalidas desde CSV con indice {index:d}')
def step_ingreso_credenciales_invalidas_csv(context, index):
    """Cuando ingreso credenciales invalidas desde el CSV de errores"""
    user = get_user_by_index(context.invalid_users, index)
    # Usar .get(key, "") para evitar errores si la celda esta vacia
    email = user.get("email", "").strip()
    password = user.get("password", "").strip()
    
    context.login_page.enter_username(email)
    context.login_page.enter_password(password)
    context.login_page.click_login()


@then('deberia ver el mensaje de bienvenida')
def step_ver_mensaje_bienvenida(context):
    """Entonces deberia ver el mensaje de bienvenida"""
    assert context.login_page.is_welcome_message_visible(), "Mensaje de bienvenida no visible"

@then('deberia ver un mensaje de error')
def step_ver_mensaje_error(context):
    """Entonces deberia ver un mensaje de error"""
    assert context.login_page.get_error_message() != "", "Mensaje de error no visible o vacio"

@then('el mensaje de error deberia ser "{expected_error}"')
def step_ver_mensaje_error_especifico(context, expected_error):
    """Entonces el mensaje de error deberia ser el esperado"""
    actual_error = context.login_page.get_error_message()
    assert expected_error in actual_error, f"Error esperado: '{expected_error}', se obtuvo: '{actual_error}'"