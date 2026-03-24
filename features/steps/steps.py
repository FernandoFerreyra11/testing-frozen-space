from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
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


# --- Pasos de Registro ---

@given('estoy en la pagina de registro')
def step_estoy_en_pagina_registro(context):
    """Dado que estoy en la pagina de registro"""
    context.register_page = RegisterPage(context.driver)
    context.register_page.navigate_to_register()
    # Asegurar que estamos en modo registro si hay un toggle
    context.register_page.click_registrate_aqui()


@when('ingreso el nombre completo "{name}"')
def step_ingreso_nombre_completo(context, name):
    """Cuando ingreso el nombre completo"""
    context.register_page.enter_full_name(name)


@when('ingreso un email nuevo "{email}"')
def step_ingreso_email_nuevo(context, email):
    """Cuando ingreso un email nuevo"""
    context.register_page.enter_email(email)


@when('ingreso una contraseña "{password}"')
def step_ingreso_password(context, password):
    """Cuando ingreso una contraseña"""
    context.register_page.enter_password(password)


@when('hago clic en registrar')
def step_hacer_clic_registrar(context):
    """Cuando hago clic en registrar"""
    context.register_page.click_register()


@when('ingreso datos de registro desde CSV con indice {index:d}')
def step_ingreso_datos_registro_csv(context, index):
    """Cuando ingreso datos de registro desde el CSV de registros"""
    user = get_user_by_index(context.register_users, index)
    name = user.get("full_name", "").strip()
    email = user.get("email", "").strip()
    password = user.get("password", "").strip()
    
    context.register_page.enter_full_name(name)
    context.register_page.enter_email(email)
    context.register_page.enter_password(password)
    context.register_page.click_register()


@then('deberia ver un mensaje de éxito "{expected_message}"')
def step_ver_mensaje_exito(context, expected_message):
    """Entonces deberia ver un mensaje de éxito"""
    actual_message = context.register_page.get_success_message()
    assert expected_message in actual_message, f"Esperado exito: {expected_message}, Obtenido: {actual_message}"


@then('deberia ver un mensaje de error que contiene "{expected_error}"')
def step_ver_mensaje_error_registro(context, expected_error):
    """Entonces deberia ver un mensaje de error que contiene el texto esperado"""
    actual_error = context.register_page.get_error_message()
    assert expected_error in actual_error, f"Esperado error: {expected_error}, Obtenido: {actual_error}"