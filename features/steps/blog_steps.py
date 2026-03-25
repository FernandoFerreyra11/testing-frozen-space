from behave import given, when, then
from pages.blog_page import BlogPage
import time

@given('navego a la pagina del blog')
def step_navego_pagina_blog(context):
    """Dado navego a la pagina del blog"""
    context.blog_page = BlogPage(context.driver)
    context.blog_page.navigate_to_blog()
    time.sleep(2) # Esperar un poco a que se carguen los posts

@when('ingreso el titulo "{titulo}"')
def step_ingreso_titulo_blog(context, titulo):
    """"Cuando ingreso el titulo"""
    # Guardamos el titulo en el contexto por si lo necesitamos
    context.last_post_title = titulo
    context.blog_page.enter_title(titulo)

@when('ingreso el contenido "{contenido}"')
def step_ingreso_contenido_blog(context, contenido):
    """Y ingreso el contenido"""
    context.blog_page.enter_content(contenido)

@when('hago clic en publicar en el blog')
def step_hacer_clic_publicar_blog(context):
    """Y hago clic en publicar en el blog"""
    context.blog_page.click_publish()
    time.sleep(2) # Esperar a que la peticion termine y los posts se recarguen

@then('el post con titulo "{titulo}" deberia ser visible en el muro')
def step_post_visible_blog(context, titulo):
    """Entonces el post con titulo deberia ser visible en el muro"""
    is_visible = context.blog_page.is_post_visible(titulo)
    assert is_visible, f"El post con titulo '{titulo}' no esta visible en el muro de posts."
