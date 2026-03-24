Feature: Login de Usuario
  Como usuario del sistema
  Quiero poder iniciar sesión
  Para acceder a mi cuenta

  @login_exitoso
  Scenario: Login exitoso
    Given estoy en la pagina de login
    When ingreso credenciales validas
    Then deberia ver el mensaje de bienvenida

  @login_fallido
  Scenario: Login fallido con credenciales incorrectas
    Given estoy en la pagina de login
    When ingreso credenciales invalidas
    Then deberia ver un mensaje de error

  @login_csv
  Scenario: Login exitoso con credenciales del CSV
    Given estoy en la pagina de login
    When ingreso credenciales desde CSV con indice 0
    Then deberia ver el mensaje de bienvenida