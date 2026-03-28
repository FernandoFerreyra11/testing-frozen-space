from behave import given, when, then
from pages.demo_page import DemoPage
from utils.csv_utils import get_user_by_index

@given('estoy en la pagina de solicitud de demo')
def step_estoy_en_pagina_solicitud_demo(context):
    user = get_user_by_index(context.users, 0)
    context.demo_page = DemoPage(context.driver)
    context.demo_page.navigate_to_demo(user.get("email"), user.get("password"))

@when('ingreso datos en formulario de solicitud de demo desde el CSV con indice {index:d}')
def step_ingreso_datos_demo_csv(context, index):
    user = get_user_by_index(context.demo_users, index)
    context.last_demo_data = user  # Guardar para reusar en test repetido
    context.demo_page.enter_name(user.get("name"))
    context.demo_page.enter_email(user.get("email"))
    context.demo_page.enter_company(user.get("company", ""))
    context.demo_page.enter_role(user.get("role", ""))

@when('ingreso los mismos datos en formulario de solicitud de demo')
def step_ingreso_mismos_datos(context):
    user = context.last_demo_data
    context.demo_page.enter_name(user.get("name"))
    context.demo_page.enter_email(user.get("email"))
    context.demo_page.enter_company(user.get("company", ""))
    context.demo_page.enter_role(user.get("role", ""))

@when('hago clic en el boton de solicitar demo')
def step_hacer_clic_solicitar_demo(context):
    context.demo_page.click_submit()

@then('deberia ver el mensaje de alerta "{expected_text}"')
def step_ver_mensaje_alerta(context, expected_text):
    actual_text = context.demo_page.handle_alert()
    assert actual_text is not None, "No se mostro ninguna alerta"
    assert expected_text in actual_text, f"Alerta esperada: '{expected_text}', Obtenida: '{actual_text}'"

@when('acepto la alerta de exito')
def step_aceptar_alerta(context):
    # La alerta ya fue aceptada en handle_alert del paso anterior si se llamo, 
    # pero este paso puede ser util para claridad o si handle_alert no la acepto.
    pass

@when('dejo el campo de nombre vacio')
def step_dejar_nombre_vacio(context):
    context.demo_page.enter_name("")

@when('ingreso un email valido "{email}"')
def step_ingreso_email_valido(context, email):
    context.demo_page.enter_email(email)

@when('ingreso el nombre "{name}"')
def step_ingreso_nombre(context, name):
    context.demo_page.enter_name(name)

@when('ingreso un email invalido "{email}"')
def step_ingreso_email_invalido(context, email):
    context.demo_page.enter_email(email)

@then('el campo "{field_name}" deberia mostrar el mensaje de validacion "{expected_message}"')
def step_ver_mensaje_validacion(context, field_name, expected_message):
    actual_message = context.demo_page.get_validation_message(field_name)
    assert expected_message in actual_message, f"Esperado: '{expected_message}', Obtenido: '{actual_message}'"

@then('el campo "email" deberia mostrar un mensaje de validacion de formato de correo')
def step_ver_mensaje_validacion_email(context):
    actual_message = context.demo_page.get_validation_message("email")
    # Los mensajes de email varian por navegador, pero suelen contener "incluir un signo '@'" o similar.
    # Como fallback revisamos que no este vacio.
    assert actual_message != "", "No se mostro mensaje de validacion de email"
    assert "@" in actual_message or "email" in actual_message or "formato" in actual_message.lower() or "incluir" in actual_message.lower()