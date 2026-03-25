Feature: Funcionalidad del Blog

  Background:
    Given estoy en la pagina de login
    When ingreso credenciales validas
    Then deberia ver el mensaje de bienvenida

  Scenario: Crear un post exitosamente
    Given navego a la pagina del blog
    When ingreso el titulo "Prueba de Integracion Automatizada"
    And ingreso el contenido "Este es un post de prueba generado desde Behave y Selenium para validar los localizadores del Blog."
    And hago clic en publicar en el blog
    Then el post con titulo "Prueba de Integracion Automatizada" deberia ser visible en el muro
