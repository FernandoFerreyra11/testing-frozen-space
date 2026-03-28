Feature: Solicitud de Demo
  Como usuario del sistema
  Quiero poder solicitar una demo
  Para conocer mas sobre las capacitaciones

  @solicitud_demo_exitosa
  Scenario: Solicitud de demo exitosa
    Given estoy en la pagina de solicitud de demo
    When ingreso datos en formulario de solicitud de demo desde el CSV con indice 0
    And hago clic en el boton de solicitar demo
    Then deberia ver el mensaje de alerta "¡Solicitud enviada! Te contactaremos pronto."

  @solicitud_demo_repetida
  Scenario: Solicitud de demo repetida
    Given estoy en la pagina de solicitud de demo
    When ingreso datos en formulario de solicitud de demo desde el CSV con indice 0
    And hago clic en el boton de solicitar demo
    And acepto la alerta de exito
    When ingreso los mismos datos en formulario de solicitud de demo
    And hago clic en el boton de solicitar demo
    Then deberia ver el mensaje de alerta "Ya recibimos una solicitud de demo con estos datos, te responderemos a la brevedad. Gracias"

  @solicitud_demo_vacia
  Scenario: Validacion de campos obligatorios al dejar el nombre vacio
    Given estoy en la pagina de solicitud de demo
    When dejo el campo de nombre vacio
    And ingreso un email valido "test@example.com"
    And hago clic en el boton de solicitar demo
    Then el campo "name" deberia mostrar el mensaje de validacion "Complete este campo"

  @solicitud_demo_email_invalido
  Scenario: Validacion de formato de email incorrecto
    Given estoy en la pagina de solicitud de demo
    When ingreso el nombre "Usuario Prueba"
    And ingreso un email invalido "correo-sin-formato"
    And hago clic en el boton de solicitar demo
    Then el campo "email" deberia mostrar un mensaje de validacion de formato de correo